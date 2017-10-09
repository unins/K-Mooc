import time, os

RUN_IMAGE = [
 '''
 .ooooo.
 oo..oo.
 oo..oo.
 oo..oo.
 ooooo..''',
 '''
 ..oo...
 oooo...
 ..oo...
 ..oo...
 oooooo.''',
 '''
 .ooooo.
 o...oo.
 ..ooo..
 ooo....
 oooooo.''',
 '''
 .ooooo.
 ....oo.
 .oooo..
 ...ooo.
 ooooo..''',
 '''
 ...oo..
 .oo.o..
 oo..o..
 oooooo.
 ....o..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 ....oo.
 ooooo..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 oo..oo.
 .oooo..''',
 '''
 oooooo.
 o...oo.
 ...oo..
 ..oo...
 .oo....''',
 '''
 .ooooo.
 oo..oo.
 .oooo..
 oo..oo.
 .oooo..''',
 '''
 .ooooo.
 oo...o.
 oooooo.
 ....oo.
 ooooo..''',
 ]

for n in range(len(RUN_IMAGE)):
    pedf = RUN_IMAGE[n].replace('.', '∵').replace('o', '■').strip().split('\n')
    print(pedf)
    RUN_IMAGE[n] = pedf

for m in range(len(RUN_IMAGE)):
    for n in range(len(RUN_IMAGE)):
        os.system('cls')
        for x in range(len(RUN_IMAGE[-m-1])):
            print(RUN_IMAGE[-m-1][x].strip(),end="\t")
            print(RUN_IMAGE[-n-1][x].strip())
        time.sleep(0.1)
