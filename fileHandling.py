# create file in strict mode

# try:
#     file=open("strict.txt",'x')
#     print("File created...")
# except Exception as e:
#     print("File nhi ban sakta hai....")

try:
    file=open("write.txt",'w+')
    file.write("This is python file...")
except Exception as e:
    print("File nhi ban sakta hai....")
finally:
    file.seek(0)
    r=file.read(4)
    print(f"file content: {r}")
    file.flush()
    file.close()