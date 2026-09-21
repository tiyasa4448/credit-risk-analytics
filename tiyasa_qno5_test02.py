input_file=open("INPUT.txt","r")
output_file=open("OUTPUT.txt","w")
lines=input_file.readline()
s=" "
for i in lines:
    if i == ".":
        s=s+i+"/n"+"====="+"/n"
    else:
        s=s+i
lines=s.split('/n')
for i in lines:
    output_file.write(i)
    output_file.write('\n')

