def kwargsAcceptFun(**kwargs):
    print("Here are the keyword arguments:")
    for i in kwargs:
        print(i, "=>", kwargs[i])
kwargsAcceptFun(name="Farhod", age=20, school="NEWUU", level="Bachelor's")
