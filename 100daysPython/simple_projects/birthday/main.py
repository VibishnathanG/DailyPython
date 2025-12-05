# import smtplib

# my_email = "shadowknightt2019@gmail.com"
# password = "gvnm swmj xkzs zzbq"
# to_email = "vibishdevops@gmail.com"
# subject = "Happy Birthday!"
# body = "Wishing you a day filled with happiness and a year filled with joy. Happy Birthday!"
# message = f"Subject: {subject}\n\n{body}"
# # with smtplib.SMTP("smtp.gmail.com") as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
# #     print("Email sent successfully!")



# test1 = smtplib.SMTP("smtp.gmail.com")
# test1.starttls()
# test1.login(user=my_email, password=password)
# test1.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
# print("Email sent successfully!")
# test1.close()

class animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"{self.name} the {self.species} says {sound}"


dog = animal("Buddy", "Dog")

print(type(dog))