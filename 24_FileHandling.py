"""
file=open('python01.txt','w')
#print(file.name)
#print(file.mode)
#print(file.readable())
#print(file.writable())
#file.close()
#print(file.closed)
file.write('balaji\tKrishnan')
file.write('\n')
file.write('Python Developer')
file.close()
email_list=['garland@live.com','garland@optonline.net','psharpe@sbcglobal.net','starstuff@comcast.net','parrt@me.com']
f=open('python01.txt','w')
for x in email_list:
	f.write(x+'\n')
print('file writting Sucessfull')
f.close()
"""

