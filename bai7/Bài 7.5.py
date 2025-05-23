print("Cao Văn Dũng")
print("MSSV:235752020710031")
print("#####################")
def file_read(fname):
 from itertools import islice
 with open(fname, "w") as myfile:
  myfile.write("Python Exercises\n")
  myfile.write("Java Exercises")
 txt = open(fname)
 print(txt.read())
file_read('D:/a.txt')

