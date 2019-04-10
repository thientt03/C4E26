def string_with_no_dollars(s):
        s = s.translate({ord("$"):None})
        return(s)

string_with_no_dollars = string_with_no_dollars("$80% percent of $life is to show $up")

if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
