from tkinter import *

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    gender_info = gender.get()
    hobby_info = hobby.get()
    live_info = live.get()
    education_info = education.get()
    food_info = food.get()
    book_info = book.get()
    singer_info = singer.get()

    print(firstname_info, lastname_info, age_info, gender_info, hobby_info, live_info, education_info, food_info, book_info, singer_info)

    with open("user.txt", "a") as file:
        file.write("Firstname: " + firstname_info + "\n")
        file.write("Lastname: " + lastname_info + "\n")
        file.write("Age: " + str(age_info) + "\n")
        file.write("Gender: " + gender_info + "\n")
        file.write("Hobby: " + hobby_info + "\n")
        file.write("Live: " + live_info + "\n")
        file.write("Education: " + education_info + "\n")
        file.write("Food: " + food_info + "\n")
        file.write('Book: ' + book_info + "\n")
        file.write("Singer: " + singer_info + "\n")
        file.close()

screen = Tk()
screen.geometry("500x900")
screen.title("Survey Form")
heading = Label(text="Survey Form", bg="grey", fg="black", width="500", height="3")
heading.pack()

firstname_label = Label(text="What is your Firstname * ")
lastname_label = Label(text="What is your Lastname * ")
age_label = Label(text="What is your Age * ")
gender_label = Label(text="What is your Gender * ")
hobby_label = Label(text="What is your Hobby * ")
live_label = Label(text="Where do you live? *")
education_label = Label(text="What are your education qualifications? *")
food_label = Label(text="What is your favourite dish * ")
book_label = Label(text="What is the name of your favourite book? *")
singer_label = Label(text="Who is your Favourite Singer? *")

firstname_label.place(x=15, y=70)
lastname_label.place(x=15, y=140)
age_label.place(x=15, y=210)
gender_label.place(x=15, y=280)
hobby_label.place(x=15, y=350)
live_label.place(x=15, y=420)
education_label.place(x=15, y=490)
food_label.place(x=15, y=560)
book_label.place(x=15, y=630)
singer_label.place(x=15, y=700)

firstname = StringVar()
lastname = StringVar()
age = IntVar()
gender = StringVar()
hobby = StringVar()
live = StringVar()
education = StringVar()
food = StringVar()
book = StringVar()
singer = StringVar()

firstname_entry = Entry(textvariable=firstname)
lastname_entry = Entry(textvariable=lastname)
age_entry = Entry(textvariable=age)
gender_entry = Entry(textvariable=gender)
hobby_entry = Entry(textvariable=hobby)
live_entry = Entry(textvariable=live)
education_entry = Entry(textvariable=education)
food_entry = Entry(textvariable=food)
book_entry = Entry(textvariable=book)
singer_entry = Entry(textvariable=singer)

firstname_entry.place(x=250, y=70)
lastname_entry.place(x=250, y=140)
age_entry.place(x=250, y=210)
gender_entry.place(x=250, y=280)
hobby_entry.place(x=250, y=350)
live_entry.place(x=250, y=420)
education_entry.place(x=250, y=490)
food_entry.place(x=250, y=560)
book_entry.place(x=250, y=630)
singer_entry.place(x=250, y=700)

Save = Button(screen, text="Save Response", width="30", height="2", command=save_info, bg="grey")
Save.place(x=15, y=760)

screen.mainloop()
