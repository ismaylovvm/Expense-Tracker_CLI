import sys
import datetime
import datafile_options

arguments = sys.argv


class expense():

    def __init__(self,id,command,description,amount):

        self.command = command 
        self.description = description
        self.amount = amount
        self.id = id

        curr_time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.time = curr_time
 
        


    def get_dict(self):

        return {
            "ID" : self.id,
            "Command" : self.command,
            "Description" : self.description,
            "Amount" : self.amount,
            "Date" : self.time

        }


if arguments[1] == "add":

    cmd = arguments[1]
    dscpt = arguments[3]
    amt = arguments[5]

    datafile =  datafile_options.get_database()

    if len(datafile) == 0:
        curr_id = 1
    else:
        max = 0
        for data in datafile:
            if data["ID"] > max:
                max = data["ID"]
        curr_id = max + 1


    new_expense = expense(curr_id,cmd,dscpt,amt).get_dict()

    datafile.append(new_expense)

    datafile_options.write_database(datafile)


elif arguments[1] == "list":

    datafile =  datafile_options.get_database()
    
    print("#        ID           Date           Description           Amount")
    for exp in datafile:
        print(f"# {exp['ID']}  {exp['Date']}  {exp['Description']}  {exp['Amount']}")



elif arguments[1] == "summary":

    datafile =  datafile_options.get_database()
    flag = 0

    sumofexp = 0

    if len(arguments) == 4:

        for exp in datafile:
            
            date = datetime.datetime.strptime(exp["Date"],"%Y-%m-%d")
            if date.month == int(arguments[3]):
                sumofexp += float(exp["Amount"])
        
        print(f"Total expenses for {arguments[3]}th month: ${sumofexp}")
        flag = 1
    
    else:

        for exp in datafile:
            sumofexp += float(exp["Amount"])
        print(f"Total expenses: ${sumofexp}")
        flag = 1

    if flag == 0:
        print("Control arguments")
        sys.exit(1)


elif arguments[1] == "update":

    req_id = arguments[3]

    datafile = datafile_options.get_database()

    flag = 0

    for data in datafile:
        if data["ID"] == int(req_id):
            data["Amount"] = arguments[5]
            flag = 1
    datafile_options.write_database(datafile)

    if flag == 0:
        print("Cannot find ID")
        sys.exit(1)

    


        
elif arguments[1] == "delete":

    req_id = arguments[3]

    datafile = datafile_options.get_database()

    flag = 0

    for data in datafile:
        if data["ID"] == int(req_id):
            datafile.remove(data)
            flag = 1
    datafile_options.write_database(datafile)

    if flag == 0:
        print("Cannot find ID")
        sys.exit(1)





    
            
            