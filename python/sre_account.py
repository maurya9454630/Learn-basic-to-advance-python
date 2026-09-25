
import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            print("No such file exists. Starting with empty database.")

    except Exception as err:
        print(f"An exception occurred: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            # json.dump(Bank.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_latters,k = 3)
        num = random.choices(string.digits,k = 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id)


    def Createaccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("Tell your 4 number PIN: ")),
            "account": random.randint(100000, 999999),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry, you cannot create your account.")
        else:
            print("Account has been created successfully.")

            for i in info:
                print(f"{i} : {info[i]}")

            print("Please note down your account number.")

            Bank.data.append(info)

            Bank.__update()


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for depositing money in the bank")
print("Press 3 for withdrawing money")
print("Press 4 for details")
print("Press 5 for updating details")
print("Press 6 for deleting your account")

check = int(input("Tell your response: "))

if check == 1:
    user.Createaccount() 

