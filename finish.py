import sqlalchemy as sqll
import pymysql
import time
import board
import neopixel
 


pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 156

# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

sektor = ( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 
[24, 25, 26],
[27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
[47, 48, 49, 50, 51, 52, 53, 54],
[55, 56,147, 148],
[57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68],
[69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
[82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
[110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126],
[127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148] )

pixels.fill((0, 255, 0))
pixels.show()


HOST = '172.19.3.56'
PORT = 33006


mysql_creds = {
    "user": "ctfd",
    "password": "ctfd",
    "host": "localhost",
    "db": "ctfd"
}


engine = sqll.create_engine('mysql+pymysql://ctfd:ctfd@172.19.3.56:33006/ctfd')


while True:
    with engine.connect() as conn:
        current_state = conn.execute(sqll.text('''
        select distinct challenge_id as solved, challenges.id as task from solves right join challenges on solves.challenge_id=challenges.id
        '''))
        count = 0
        for row in current_state:
            #print(row["solved"])
            if row[0] != None:
                count += 1
                solvedd = row[0] 
                for i in range(num_pixels):
                    if i in sektor[solvedd]:
                        pixels[i] = (255,0,0)
                        pixels.show()
        if count == 0:
            pixels.fill((0, 255, 0))
            pixels.show()