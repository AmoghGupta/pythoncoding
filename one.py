
def myfunc():
    print("Function in one.py")
    
print("TOP LEVEL IN ONE.PY")

# if you ever run a python file directly then 
# this case becomes true
if __name__ == "__main__":
    print('ONE.PY is being run  directly!')
else:
    print('ONE.PY has been imported!!')
    
