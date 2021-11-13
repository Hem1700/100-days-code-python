#Dictionaries

#{key : value}

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",  }

print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"]=  "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_dict = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary 
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)


# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])




# Day-9-1 Exercise

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades= {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >=71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"        


print(student_grades)




# Nesting

capitals = {
    "France": "Paris",
    "Germany" : "Berlin"

}

travel_log = {
    "France": {"cities_visited":['Paris', 'Lille', 'Dijon'], "total_visits": 12 },
    "Germany" :{"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
}
print(travel_log)


# Day-9-2 Exercise

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_visited, times_visited, cities_visited):
    empty_dict = {}
    empty_dict["country"] = country_visited,
    empty_dict["visits"] = times_visited,
    empty_dict["cities"] = cities_visited,
    travel_log.append(empty_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)    
