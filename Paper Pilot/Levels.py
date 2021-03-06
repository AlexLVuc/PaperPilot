from random import *

###############################
## LEVEL RELATED INFORMATION ##
###############################

#WHIP:      xPos, yPos, frames
#WAVE:      xPos, yPos, directionY, frames
#RANDOM:    xPos, yPos, xMove, frequency, frames
#RANDOMV2:  xPos, yPos, frequency, frames
#SPIRAL:    xPos, yPos, startAngle, endAngle, frequency
#CIRCLE:    xPos, yPos, numBullets, speed, frequency
#WAVELINE:  xPos, yPos, startXPos, endXPos, jump, frequency, frames
#HOMING:    xPos, yPos, speed, frequency, frames
#LINE:      xPos, yPos, End, direction, moveSpeed, frames
#WALL:      xPos, yPos, numBullets, frequency, frames



level1 = {560: [["Wall",[0,20,20,100,500]]],
         30: [["Wall",[0,20,20,150,500]]],
         1090: [["Wall",[0,20,20,50,500]]],
         1675: [["Wall",[0,20,20,35,250]]]}

level2 = {30: [["Wave",[250,780,1,100]]],
          160: [["Wave",[250,20,0,100]]],
          300: [["Whip",[250,5,75]]],
          450: [["Whip",[150,5,75]],["Whip",[300,5,75]]],
          650: [["Circle",[20,400,20,5,2]],["Circle",[480,400,20,5,2]]],
          800: [["Whip",[250,5,75]]],
          950: [["Wall",[0,20,20,50,500]]],
          1550: [["Wave",[250,20,0,100]]],
          1650: [["Whip",[120,5,75]]],
          1750: [["Whip",[240,5,75]]],
          1850: [["Whip",[360,5,75]]]}

level3 = {30: [["Random",[250,5,-5,5,400]],["Random",[250,5,5,5,400]]],
          600: [["RandomV2",[250,5,5,400]]],
          1100: [["Random",[100,5,5,10,400]],["Random",[200,5,5,10,400]],["Random",[300,5,5,10,400]],["Random",[400,5,5,10,400]]],
          1700: [["Whip",[250,5,75]]],
          1800: [["RandomV2",[250,5,5,150]]]}

level4 = {30: [["Homing",[250,5,5,20,100]]],
          150: [["Homing",[250,5,5,15,150]]],
          300: [["Homing",[250,5,5,10,200]]],
          500: [["Homing",[250,5,5,5,250]]],
          750: [["Homing",[175,5,5,15,200]],["Homing",[350,5,5,15,200]]],
          1000: [["Homing",[250,5,3,30,300]]],
          1007: [["Homing",[250,795,3,30,300]]],
          1015: [["Homing",[5,400,3,30,300]]],
          1023: [["Homing",[495,400,3,30,300]]],
          1400: [["Homing",[5,5,3,30,300]]],
          1407: [["Homing",[5,795,3,30,300]]],
          1415: [["Homing",[495,5,3,30,300]]],
          1423: [["Homing",[495,795,3,30,300]]],
          1700: [["Homing",[230,795,5,15,300]],["Homing",[250,795,5,15,250]],["Homing",[270,795,5,15,250]]]}

level5 = {30: [["WaveLine",[0,20,0,150,15,4,400]],["WaveLine",[150,20,150,300,15,4,400]],["WaveLine",[300,20,300,450,15,4,400]],["WaveLine",[450,20,450,600,15,4,400]]],
          500: [["Circle",[20,20,20,5,2]]],
          525: [["Circle",[100,20,20,5,2]]],
          550: [["Circle",[200,20,20,5,2]]],
          575: [["Circle",[300,20,20,5,2]]],
          600: [["Circle",[400,20,20,5,2]]],
          625: [["Circle",[480,20,20,5,2]]],
          700: [["Spiral",[250,780,0,360,10]],["Spiral",[250,780,120,460,10]],["Spiral",[250,780,240,600,10]]],
          701: [["Circle",[250,20,15,5,2]]],
          850: [["Circle",[250,20,15,5,2]]],
          1000: [["Circle",[250,20,15,5,2]]],
          1200: [["Homing",[250,20,5,40,400]],["Homing",[20,400,5,40,400]],["Homing",[480,400,5,40,400]]],
          1650: [["WaveLine",[0,20,0,150,15,4,300]],["WaveLine",[150,20,150,300,15,4,300]],["WaveLine",[300,20,300,450,15,4,300]],["WaveLine",[450,20,450,600,15,4,300]]]}
        

level6 = {30: [["Homing",[20,20,5,20,400]],["Homing",[150,20,5,20,400]],["Homing",[300,20,5,20,400]],["Homing",[450,20,5,20,400]]],
          500: [["Homing",[20,200,5,20,400]],["Homing",[20,400,5,20,400]],["Homing",[20,600,5,20,400]]],
          1000: [["Homing",[20,780,5,20,400]],["Homing",[150,780,5,20,400]],["Homing",[300,780,5,20,400]],["Homing",[450,780,5,20,400]]],
          1500: [["Homing",[480,200,5,20,400]],["Homing",[480,400,5,20,400]],["Homing",[480,600,5,20,400]]]}

level7 = {30: [["Homing",[20,20,5,20,400]]],
              60: [["Homing",[480,20,5,20,400]]],
              200: [["Circle",[250,20,25,5,2]]],
              300: [["Circle",[100,20,25,5,2]]],
              301: [["Circle",[400,20,25,5,2]]],
              500: [["Wave",[250,20,0,100]]],
              750: [["Spiral",[250,20, 0, 360, 2]]],
              751: [["Homing",[10,400,2,20,100]]],
              752: [["Homing",[490,400,2,20,100]]],
              850: [["Circle",[randint(100,400),20,25,5,2]]],
              875: [["Circle",[randint(100,400),20,25,5,2]]],
              900: [["Circle",[randint(100,400),20,25,5,2]]],
              925: [["Circle",[randint(100,400),20,25,5,2]]],
              950: [["Circle",[randint(100,400),20,25,5,2]]],
              975: [["Circle",[randint(100,400),20,25,5,2]]],
              1101: [["Random",[20,20,10,10,450]]],
              1102: [["Circle",[20,5,5,5,2]]],
              1150: [["Circle",[20,5,10,5,2]]],
              1200: [["Circle",[20,5,15,5,2]]],
              1250: [["Circle",[20,5,20,5,2]]],
              1350: [["Circle",[480,5,5,5,2]]],
              1400: [["Circle",[480,5,10,5,2]]],
              1450: [["Circle",[480,5,15,5,2]]],
              1500: [["Circle",[480,5,20,5,2]]],
              1600: [["Whip", [50,20,100]]],
              1650: [["Whip", [250,20,100]]],
              1700: [["Whip", [450,20,100]]],}

level8 = {30: [['Spiral', [250, 20, 0, 360, 20]], ['Spiral', [250, 20, 120, 480, 20]], ['Spiral', [250, 20, 240, 600, 20]]],
          31: [['Spiral', [100, 50, 0, 360, 20]], ['Spiral', [100, 50, 120, 480, 20]], ['Spiral', [100, 50, 240, 600, 20]]],
          32: [['Spiral', [400, 50, 0, 360, 20]], ['Spiral', [400, 50, 120, 480, 20]], ['Spiral', [400, 50, 240, 600, 20]]],
          40: [['Circle', [randint(100,400), 20,20, 5, 1]]],
          100: [['Circle', [randint(100,400), 20,20,5, 1]]],
          140: [['Circle', [randint(100,400), 20,20,5, 1]]],
          180: [['Circle', [randint(100,400), 20,20,5, 1]]],
          250: [['Circle', [200, 20,20,5, 1]]],
          251: [['Circle', [400, 20,20,5, 1]]],
          350: [['Circle', [100, 20,20,5, 1]]],
          351: [['Circle', [200, 20,20,5, 1]]],
          352: [['Circle', [300, 20,20,5, 1]]],
          353: [['Circle', [400, 20,20,5, 1]]],
          500: [["Wave",[250,20,0,75]]],
          1000: [["Spiral",[20,400,0,360,20]]],
          1001: [["Spiral",[480,400,180,540, 20]]],
          1150: [["RandomV2",[250,20,4,150]]],
          1450: [["Wave",[250,20,0,200]], ["Homing",[10,250,2,10,100]], ["Homing",[490,250,2,10,100]]]}

level9 = {100: [["Circle",[10,10,15,5,2]]],
              150: [["Circle",[10,100,15,5,2]]],
              200: [["Circle",[10,200,15,5,2]]],
              250: [["Circle",[10,300,15,5,2]]],
              300: [["Circle",[10,400,15,5,2]]],
              350: [["Circle",[10,500,15,5,2]]],
              400: [["Circle",[10,600,15,5,2]]],
              450: [["Circle",[10,700,15,5,2]]],
              500: [["Circle",[10,790,15,5,2]]],
              550: [["Circle",[100,790,15,5,2]]],
              600: [["Circle",[200,790,15,5,2]]],
              650: [["Circle",[300,790,15,5,2]]],
              700: [["Circle",[400,790,15,5,2]]],
              750: [["Circle",[490,790,15,5,2]]],
              800: [["Circle",[490,700,15,5,2]]],
              850: [["Circle",[490,600,15,5,2]]],
              900: [["Circle",[490,500,15,5,2]]],
              950: [["Circle",[490,400,15,5,2]]],
              1000: [["Circle",[490,300,15,5,2]]],
              1050: [["Circle",[490,200,15,5,2]]],
              1100: [["Circle",[490,100,15,5,2]]],
              1150: [["Circle",[490,10,15,5,2]]],
              1200: [["Circle",[400,100,15,5,2]]],
              1250: [["Circle",[300,100,15,5,2]]],
              1300: [["Circle",[200,100,15,5,2]]],
              1350: [["Circle",[100,100,15,5,2]]],
              1400: [["Circle",[10,100,15,5,2]]],
              1500: [["Circle",[10,10,7,5,2]], ["Circle",[490,10,7,5,2]]],
              1550: [["Circle",[10,100,7,5,2]], ["Circle",[490,100,7,5,2]]],
              1600: [["Circle",[10,200,7,5,2]], ["Circle",[490,200,7,5,2]]],
              1650: [["Circle",[10,300,7,5,2]], ["Circle",[490,300,7,5,2]]],
              1700: [["Circle",[10,400,7,5,2]], ["Circle",[490,400,7,5,2]]],
              1750: [["Circle",[10,500,7,5,2]], ["Circle",[490,500,7,5,2]]],
              1800: [["Circle",[10,600,7,5,2]], ["Circle",[490,600,7,5,2]]],
              1850: [["Circle",[10,700,7,5,2]], ["Circle",[490,700,7,5,2]]],
              1900: [["Circle",[10,790,7,5,2]], ["Circle",[490,790,7,5,2]]]}

level10 = {30: [["Line",[50,10,150,1,1,1700]]],
        31: [["Line",[450,10,350,1,1,1700]]],
        32: [["Line",[10,50,250,0,1,1700]]],
        33: [["Line",[10,750,550,0,1,1700]]],
        100: [["Homing",[250,20,3,50,1300]]],
        350: [["RandomV2",[250,20,2,150]]],
        300: [["Circle",[50,50,15,5,2]]],
        350: [["Circle",[450,50,15,5,2]]],
        400: [["Circle",[50,750,15,5,2]]],
        450: [["Circle",[450,750,15,5,2]]],
        500: [["Circle",[50,50,15,5,2]]],
        525: [["Circle",[450,50,15,5,2]]],
        550: [["Circle",[50,750,15,5,2]]],
        575: [["Circle",[450,750,15,5,2]]],
        750: [["Spiral",[50,50, 0, 360, 2]]],
        751: [["Spiral",[450,50, -120, 240, 4]]],
        752: [["Spiral",[50,750, -240,120, 4]]],
        753: [["Spiral",[450,750, -360, 0, 4]]],
        1000: [["RandomV2",[250,20,5,200]]],
        1300: [["WaveLine",[0,20,0,80,15,6,400]],["WaveLine",[80,20,80,160,15,6,400]],["WaveLine",[160,20,160,240,15,6,400]],["WaveLine",[240,20,240,320,15,6,400]],["WaveLine",[320,20,320,400,15,6,400]],["WaveLine",[400,20,400,480,15,6,400]]],
        1800: [["Homing", [20,5,5,5,150]],["Homing", [80,5,5,5,150]],["Homing", [140,5,5,5,150]],["Homing", [200,5,5,5,150]],["Homing", [260,5,5,5,150]],["Homing", [320,5,5,5,150]],["Homing", [380,5,5,5,150]],["Homing", [440,5,5,5,150]],["Homing", [500,5,5,5,150]]]}
                     
levels = []
levels.append(level1)
#BEAT LEVEL 1:
#Conner
#Gaurav
#Sagar
#James
#Dinka

levels.append(level2)
#BEAT LEVEL 2:
#Not Class Tested

levels.append(level3)
#BEAT LEVEL 3:
#Not Class Tested

levels.append(level4)
#BEAT LEVEL 4:
#Not Class Tested

levels.append(level5)
#BEAT LEVEL 3:
#Not Class Tested

levels.append(level6)
#BEAT LEVEL 6:
#Not Class Tested

levels.append(level7)
#BEAT LEVEL 7:
#Gaurav
#Sourav

levels.append(level8)
#BEAT LEVEL 8:
#Dinka
#Gaurav
#Sourav

levels.append(level9)
#BEAT LEVEL 9:
#Sagar

levels.append(level10)
#BEAT LEVEL 10:
#Conner
#Dinka

