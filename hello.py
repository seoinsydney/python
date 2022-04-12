print("hello from notepad")
print(2+2)
# this is comments

red_box = "Seo"
red_box = 10

# delete variable
# del red_box 

print(red_box)
print(type(red_box))

# if else statement
seo_age = 31
boris_age = 35

if seo_age < boris_age:
    print("boris is older")
elif seo_age == boris_age:
    print("same age")
else:
    print("seo is older")

# function 

def print_weather(text):
    # text = "isn't it rainy outside?"
    print(text)
    print(text)
    print(text)

print_weather("isn't it rainy outside?")


def school_age_calculator(age, name):
    if age < 5:
        print("You are still young!", name, "is only", age)
    elif age == 5:
        print("Enjoy kindergarten", name)
    else:
        print("kids grow up so fast!")

school_age_calculator(3, "Boris")