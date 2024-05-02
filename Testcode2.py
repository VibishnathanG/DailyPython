s="{}[]()}{"

c_list= [*s]



if c_list.count("(") == c_list.count(")") and c_list.count("{") == c_list.count("}") and c_list.count("[") == c_list.count("]") :
    print("yes")
else:

    print("No")



