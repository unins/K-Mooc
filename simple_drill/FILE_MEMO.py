import sys,os

os.system('cls')

# [TEST argv] --------------------------------------------------------------
# print(sys.argv)
#
# for n in range(len(sys.argv)):
#     print('sys.argv[%s]='%(n),sys.argv[n])
#
# print(len(sys.argv))
# <class 'list'> command='1', arg1='2' arg2='3'

# print('sys.argv=',sys.argv)         #['memo.py', 'dd','dd']
# print('len=',len(sys.argv))         #['memo.py', 'dd','dd']
#
# for n in range(len(sys.argv)):
#     print('sys.argv[%s]='%n, sys.argv[n])         #['memo.py', 'dd','dd']
#
# print(type(sys.argv))           #['D:\..\.memo.py', 'dd','dd'] .. include {PATH}
# print(len(sys.argv))            #f
#
# [body] --------------------------------------------------------------

DESTIN_DIR='../static/data_doc/'
MY_MEMO = 'memo.pdb'

HELP_MESSAGE='''\n\n\
====================================================
           MEMO.PY -- HELP MESSAGE
---------------------------------------------------
This is simple example of read & write file funtion

USAGE:    python memo.py {mode}, [args1]
=====
   -a --append:     ADD Memo = args1
   -v --verbose:    VIEW Memo w/o args1
----------------------------------------------------
'''

HEADER='''\n
====================================================
        %s
----------------------------------------------------'''

if len(sys.argv) < 2:
    print('\n*** ERROR: YOU NEED MORE THEN 1 ARGV(OPTION)! ***')
    print(HELP_MESSAGE)
    raise SystemExit(1)
else:
    option = sys.argv[1]
    MESSAGE = "MEMO OPTION: "+option
    print(HEADER % MESSAGE)

if option == '-h' or option == '--help':
    print(HELP_MESSAGE)
elif option == '-a' or option == '--append':
    if len(sys.argv) < 3:
        print ('*** ARGV 2 MISSING ***')
    else:
        memo = sys.argv[2]
        f = open(DESTIN_DIR+MY_MEMO, 'a')
        f.write(memo+"\n")
        f.close()

elif option == '-v' or option == '--verbose':
    f = open(DESTIN_DIR+MY_MEMO, 'r')
    memo = f.read()
    f.close()
    print(memo)

else:
    print('***  OPTION IS NOT AVAILABLE!  ***')
