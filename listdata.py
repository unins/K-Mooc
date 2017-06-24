# colors = ["red","blue","green","white","black","yellow","purple","pink","orange"]
# print (colors[0])
# print (colors[2])
# print(len(colors))
# print(type(colors))
# print(colors[0:9])
# print(colors[::2])
# print(colors[:])
# print(colors[-5:-1])
# print(colors[-50:50])
# color = colors[0:5]
# color2 = colors[5:9]
# print (color)
# print (color2)
# print (color + color2)
# print (len(color))
# print (len(color2))
# print ('blue' in color2)
# print ('pink' in color2)
# all_color = color + color2
# print (all_color)
# all_color[0] = "R"
# all_color[1] = "B"
# all_color[2] = "G"
# print (all_color)
# all_color.remove("R")
# all_color.remove("B")
# all_color.remove("G")
# all_color.append("sky_blue")
# all_color.append("opera_red")
# all_color.append("navy_blue")
# all_color.insert(0,"green")
# all_color.insert(0,"blue")
# all_color.insert(0,"red")
# all_color.append("magenta")
# all_color.append("cyan")
# all_color.append("brown")
# all_color.append("oak_red")
# all_color.append("rose_red")
# print (all_color)

def LOL():
	score= '''
	+----------+-------+-------+-------+-------+-------+
	|   구분   |   A   |   B   |   C   |   D   |   E   |
	+----------+-------+-------+-------+-------+-------+
	| 문학점수 | %5s | %5s | %5s | %5s | %5s |
	+----------+-------+-------+-------+-------+-------+
	| 사회점수 | %5s | %5s | %5s | %5s | %5s |
	+----------+-------+-------+-------+-------+-------+
	| 영어점수 | %5s | %5s | %5s | %5s | %5s |
	+----------+-------+-------+-------+-------+-------+
	

	'''

	kor_score = [0, 97, 100, 65, 82]
	society_score = [0, 52, 100, 74, 87]
	english_score = [0, 69, 100, 58, 90]
	mid_term = [kor_score, society_score, english_score]

	print(score %(
		mid_term[0][0], mid_term[0][1], mid_term[0][2], mid_term[0][3], mid_term[0][4],
		mid_term[1][0], mid_term[1][1], mid_term[1][2], mid_term[1][3], mid_term[1][4],
		mid_term[2][0], mid_term[2][1], mid_term[2][2], mid_term[2][3], mid_term[2][4],
	))
	
	lmao = input()
	
	if lmao == "lol":
		LOL()
		

LOL()

#print(score)
