# cook your dish here
import sys						# to use list argv, argv[0] contains filename
infile=open(sys.argv[1],"r")    # argv[1] will have input file name, open in read mode
outfile=open(sys.argv[2],"w")   # argv[2] will have output file name, open in write mode
while True:
  x=int(infile.readline())
  if x!=42:
    outfile.write(str(x)+'\n')  #convert x to str, since write() takes a string parameter
  else:
    break
infile.close()
outfile.close()