#zomg all the libraries
import sys
import os
import platform
import string

#terminal size for formatting
ts = os.get_terminal_size()
osname = platform.system()

#check OS and clear screen by os and other stuff i did cause i was bored and avoiding real work
if osname == "Linux": 
	os.system("clear")
	linuxver = platform.linux_distribution()
	msg01 = "Trustworthily optimized for Linux " + linuxver[0] +' ' + linuxver[1] + ' by the very best southamerican coders.'
elif osname == "Windows": 
	os.system("cls")
	winvermaj = sys.getwindowsversion().major
	winvermajstr = str(winvermaj)
	winvermin = sys.getwindowsversion().minor
	winverminstr = str(winvermin)
	msg01 = "Totally optimized for Windoge " + winvermajstr +'.' + winverminstr + ' by top southamerican coders.'
else:
	msg01 = 'lol wat OS do you run brah?' + ' Wat is ' + osname


centertxt = msg01.center(ts.columns,' ')
print('\n')
print(centertxt)
print('\n\n')

	

vers = '0.1'

#full list of basic commands
watcomlist = '!help','!reg','!watstats','!watpack','!post','!defend','!work','!steal'

#syntax
errmsg = {}
errmsg['notin'] = 'Welcome to Watbot Version ' + vers + '.',''
errmsg['gral'] = 'type something pls wat. ','that''s a weird character bro. ','invalid argument. ','Wat! That''s not a command! Try !help if you\'re lost'
errmsg['help'] = 'Valid arguments are !help, !reg, !watstats, !watpack, !post, !defend, !work, !steal'
errmsg['reg'] = 'Valid arguments are new, name, delete',''
errmsg['watstats'] = 'Valid args are stat and hp',''
errmsg['watpack'] = 'Valid args are inv, equip, sell, buy, drop.',''
errmsg['post'] = 'Valid syntax is post weapon target attack',''
errmsg['defend'] = 'valid args are run or cower',''
errmsg['work'] = 'valid args are findjob, grind, quit',''
errmsg['steal'] = 'correct syntax is steal watbucks or item user',''

#ask for input
def listen(errmsg,errmod,num):
	print('---->> '+errmsg[errmod][num])
	userinput = input('---->> ' + 'Please enter a command' + '\n' + '\n' + '>>')
	return userinput
	
def isawatcommand(dirtyinput):
	if dirtyinput.startswith('!'):
		comcheck = True
	else:
		comcheck = False
	return comcheck

def stripclub(dirtyinput):
	dirtyinput = dirtyinput.rstrip()
	dirtyinput = dirtyinput.lower()
	args = dirtyinput.split()
	return args

watcommand = listen(errmsg,'notin',0)


while not( isawatcommand(watcommand) ):
	watcommand = listen(errmsg,'gral', 3)
	if isawatcommand(watcommand):
		break
		
args = stripclub(watcommand)

if (args[0] == watcomlist[0]):
	print("Commands are !help, !reg, !watstats, !watpack, !post, !defend, !work and !steal. \nSay !help command for more help! e.g. !help !reg")
elif (args[0] == watcomlist[1]):
	print("reggie")
elif (args[0] == watcomlist[2]):
	print("watstats")
elif (args[0] == watcomlist[3]):
	print("watpack bro")
elif (args[0] == watcomlist[4]):
	print("postit")
else:
	print("valid function pls")		