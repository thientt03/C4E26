def remove_str(s):
        print(s.translate({ord("$"):None}))
        return(s)
remove_str("skjdhskd$$")