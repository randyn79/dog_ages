#!/usr/bin/env python3

def dog_years(min_lifespan, max_lifespan, age, human_lifespan):


    min_year_equivalent = human_lifespan / min_lifespan
    max_year_equivalent = human_lifespan /max_lifespan
    min_human_age = age * min_year_equivalent
    max_human_age = age * max_year_equivalent

    return min_year_equivalent, max_year_equivalent, min_human_age, max_human_age


if __name__ == "__main__":
    min_lifespan = float(input('What is the minimum lifespan for your breed of dog? ').casefold())
    max_lifespan = float(input('What is the maximum lifespan for your breed of dog? ').casefold())
    age = float(input('How old is your dog in human years? '))
    sex = input('Is your dog male or female? ')
    if sex == 'male':
        human_lifespan = 70.8
    elif sex == 'female':
        human_lifespan = 75.6

    min_year_equivalent, max_year_equivalent, min_human_age, max_human_age = dog_years(min_lifespan, max_lifespan, age, human_lifespan)

    print()
    print(f"You indicated your dog's breed lives between {min_lifespan} and {max_lifespan} human years.")
    print()
    print(f"This indicates that for every one human year (based on sex) your pet ages between ")
    print(f"{max_year_equivalent} and {min_year_equivalent} dog years.")
    print()
    print(f"Based on the age you entered for your dog, your dog is between ")
    print(f"{max_human_age} and {min_human_age} in dog years.")
