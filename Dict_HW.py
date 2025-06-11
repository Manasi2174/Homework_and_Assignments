# movies db for year 2022

moviesdb_2022={}

names1='Shamshera'
names2='Brahmāstra: Part One-Shiva'
names3='Gangubai Kathiawadi'

casting1=['Ranbir Kapoor','Sanjay Dutt','Vaani Kapoor']
casting2=['Ranbir Kapoor','Alia Bhatt','Amitabh Bachchan','Mouni Roy','Nagarjuna Akkineni']
casting3=['Alia Bhatt', 'Shantanu Maheshwari','Ajay Devgn']

moviesdb_2022['Shamshera']=['Ranbir Kapoor','Sanjay Dutt','Vaani Kapoor']
moviesdb_2022['Brahmāstra: Part One-Shiva']=['Ranbir Kapoor','Alia Bhatt','Amitabh Bachchan','Mouni Roy','Nagarjuna Akkineni']
moviesdb_2022['Gangubai Kathiawadi']=['Alia Bhatt', 'Shantanu Maheshwari','Ajay Devgn']

# print(type(moviesdb_2022),moviesdb_2022)

# movies db for year 2023
moviesdb_2023={}

names4='Tu Jhoothi Main Makkaar'
names5='Rocky Aur Rani Kii Prem Kahaani'
names6='Animal'

casting4=['Ranbir Kapoor', 'Shraddha Kapoor',' Dimple Kapadia', 'Boney Kapoor', 'Anubhav Singh Bassi']
casting5=['Ranveer Singh',' Alia Bhatt', 'Shabana Azmi',' Jaya Bachchan']
casting6=['Anil Kapoor', 'Bobby Deol', 'Rashmika Mandanna',' Triptii Dimri','Ranbir Kpoor' ]

moviesdb_2023['Tu Jhoothi Main Makkaar']=['Ranbir Kapoor', 'Shraddha Kapoor',' Dimple Kapadia', 'Boney Kapoor', 'Anubhav Singh Bassi']
moviesdb_2023['Rocky Aur Rani Kii Prem Kahaani']=['Ranveer Singh',' Alia Bhatt', 'Shabana Azmi',' Jaya Bachchan']
moviesdb_2023['Animal']=['Anil Kapoor', 'Bobby Deol', 'Rashmika Mandanna',' Triptii Dimri','Ranbir Kpoor' ]

# print(moviesdb_2023)

# movies db for year 2024
moviesdb_2024={}

names7=' Stree 2'
names8=' Bhool Bhulaiyaa 3 '
names9='Crew'

casting7=['Shraddha Kapoor', 'Rajkummar Rao',' Pankaj Tripathi', 'Abhishek Banerjee',' Aparshakti Khurana', 'Tamannaah Bhatia']
casting8=['Kartik Aaryan', 'Vidya Balan', 'Madhuri Dixit',' Triptii Dimri']
casting9=['Tabu', 'Kareena Kapoor Khan', 'Kriti Sanon' ]

moviesdb_2024['Stree 2']=['Shraddha Kapoor', 'Rajkummar Rao',' Pankaj Tripathi', 'Abhishek Banerjee',' Aparshakti Khurana', 'Tamannaah Bhatia']
moviesdb_2024['Bhool Bhulaiyaa 3']=['Kartik Aaryan', 'Vidya Balan', 'Madhuri Dixit',' Triptii Dimri']
moviesdb_2024['Crew']=['Tabu', 'Kareena Kapoor Khan', 'Kriti Sanon' ]

# print(moviesdb_2024)

# movies db for year 2025
moviesdb_2025={}

names10='Housefull 5'
names11='Kesari Chapter 2'
names12='Azaad'

casting10=['Akshay Kumar', 'Abhishek Bachchan', 'Riteish Deshmukh',' Sanjay Dutt', 'Jacqueline Fernandez']
casting11=['Akshay Kumar',' R. Madhavan',' Ananya Panday']
casting12=['Ajay Devgn',' Amaan Devgn',' Diana Penty']

moviesdb_2025['Housefull 5']=['Akshay Kumar', 'Abhishek Bachchan', 'Riteish Deshmukh',' Sanjay Dutt', 'Jacqueline Fernandez']
moviesdb_2025['Kesari Chapter 2']=['Akshay Kumar',' R. Madhavan',' Ananya Panday']
moviesdb_2025['Azaad']=['Ajay Devgn',' Amaan Devgn',' Diana Penty']

print(moviesdb_2025)

# Creating Big dictinoary 

Big_dict={}

Big_dict[2022]=moviesdb_2022
Big_dict[2023]=moviesdb_2023
Big_dict[2024]=moviesdb_2024
Big_dict[2025]=moviesdb_2025

print(type(Big_dict),Big_dict)

# Slicing the Big dict
print(Big_dict[2022][names1])    # ['Ranbir Kapoor','Sanjay Dutt','Vaani Kapoor']
print(Big_dict[2023][names6])    # ['Anil Kapoor', 'Bobby Deol', 'Rashmika Mandanna',' Triptii Dimri','Ranbir Kpoor']
print(Big_dict[2024])

# Displaying all keys 
print(Big_dict.keys())   #dict_keys([2022, 2023, 2024, 2025])

# Displaying all the values
print(Big_dict.values())

# Displaying key-value pairs
print(Big_dict.items())

# Iterating in Big dict
for year, movie_dict in Big_dict.items():
    print("\nMovies in :",year)
    for movie, cast in movie_dict.items():
        print(movie)
        for actor in cast:
            print("    -",actor)


# Displaying the movies and their count in which Ranbir kapoor is casted
count=0
for year,movie_dict in Big_dict.items():
    for movie,cast in movie_dict.items():
        for actor in cast:
            if actor=='Ranbir Kapoor':
             print(movie)
             count+=1
print("Total count of movies done by Ranbir Kapoor =",count)

# Displaying the castings for Stree 2 and Animal movie
for year,movie_dict in Big_dict.items():
    for movie,cast in movie_dict.items():
        if movie=='Stree 2':
         print("Actors Casted in Stree 2 are:\n",cast)







    