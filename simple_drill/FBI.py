import os,time
os.system('cls')
DESTIN_DIR ='../static/data_doc/log/'
DATA = 'database.txt'

#FBI_FILES_____________________________________________________________________
#f = open(DESTIN_DIR + DATA, 'r', encoding='utf8')
#contents = f.read()
#contents = f.readlines()

#for n in range(len(contents)):
	#print(contents[n])
	#time.sleep(0.02)

#contents =  my_file.read().strip()      # <class 'str'> a whole txt as 1
#contents = my_file.readline().strip()  # <class 'str'> read line 1x1
#contents = my_file.readlines() # <class 'list'>

# contents = my_file.read().splitlines()  # <class 'list'>
# for n in range(contents.count('')):     # count NUM of '' = 38
#     contents.remove('')
#
# my_file.close()


# # [B.01]----------------------------------------------------------------
# with open(DESTIN_DIR+DATA,'r', encoding = 'utf8') as f:
#     i=1
#     while True:
#         line = f.readline().replace('\n','') # read line 1x1
#         if line.strip() == "":          # strip blanks both end
#             continue
#         if not line:    break
#
#         print(str(i) + ' --> ' + line)  # print line x line
#         # 37 --> And when this happens, and when we allow freedom ring,
#         i+=1                           # i=i+1

# [B.02] The same as [B.01]---------------------------------------------
# with open(DESTIN_DIR+DATA,'r', encoding = 'utf8') as f:
#     i=1
#     my_file_list = f.readlines()  # <class 'list'>
#
#     for n in range(len(my_file_list)):
#         if my_file_list[n].replace('\n','').strip() == "":
#             pass
#         else:
#             print(str(i)+' --> ' + my_file_list[n].replace('\n',''))
#         # 37 --> And when this happens, and when we allow freedom ring,
#             i+=1
 # [C.01]DATA LOGGER----------------------------------------------------------------
LOGFILE = 'count_file_log.pdb'

if not os.path.isdir(DESTIN_DIR):
    os.mkdir(DESTIN_DIR)

if not os.path.exists(DESTIN_DIR+LOGFILE):
    f = open(DESTIN_DIR+LOGFILE, 'w', encoding = 'utf8')
    f.write('*** START TO WRITE A LOG ***\n')
    f.close()

with open(DESTIN_DIR + LOGFILE, 'r', encoding = 'utf8') as f:
    LINE_NUMBER = len(f.readlines()) - 1
    print('\n'+'--'*25+'\nSTART NUMBER: %d'%(LINE_NUMBER+1))

with open(DESTIN_DIR+LOGFILE, 'a', encoding='utf8') as f:
    import random, datetime

    for i in range(1,6):
        stamp = str(datetime.datetime.now())
        value = random.random()*100000
        LINE_NUMBER +=1

        log_line = '(%s) --> %s'%(LINE_NUMBER,stamp) + '\t' + str(value) + 'IS GENERATED...\n'
        f.write(log_line)

        print('%s IS Added...' %LINE_NUMBER)
        time.sleep(1)

    print('*** NEW LOG FILE WAS CREATED!!! ***')
    print('END NUMBER: ', LINE_NUMBER)
    time.sleep(3)
