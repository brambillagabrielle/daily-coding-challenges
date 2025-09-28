def get_headings(csv):
    parsed_csv = csv.split(",")

    ind = 0
    for header in parsed_csv:
        ind_header = 0
        cont = 0
        header_wo_space = ""

        for h in header:
            if h.isalpha():
                header_wo_space += h
                cont += 1
            elif h == " " and cont > 0:
                if ind_header == len(header) - 1:
                    break
                elif header[ind_header + 1].isalpha():
                    header_wo_space += h
                    cont += 1

            ind_header += 1

        parsed_csv[ind] = header_wo_space
        ind += 1

    return parsed_csv

print("Success") if get_headings("name,age,city") == ["name", "age", "city"] else print("Failed")
print("Success") if get_headings("first name,last name,phone") == ["first name", "last name", "phone"] else print("Failed")
print("Success") if get_headings("username , email , signup date ") == ["username", "email", "signup date"] else print("Failed")