gStr = "hello world"
subStr = "hello"

isAvail = lambda gstr, subStr : gstr.startswith(subStr)

if isAvail(gStr,subStr):
    print("Starts with sub string")
else:
    print("Does not start with sub string")