import statistics as stats
def display_main_menu():
   print("Hello, please enter some numbers seperated by commas! (e.g. 5, 67, 32)")

def get_user_input():
    a = (input("Enter numbers here:"))
    a = a.split(",")
    numlist = []
    for i in a:
        i = float(i)
        numlist.append(i)
    return numlist

def calc_average_temperature(x):
    numberofentries = len(x)
    total_temp = sum(x)
    average_temp = total_temp / numberofentries
    return average_temp

def calc_min_max_temperature(x):
    intlist = []
    min_max = []
    for y in x:
        intlist.append(int(y))
    min_max = [min(intlist),max(intlist)]
    return min_max
    
def calc_median_temperature(x):
    return stats.median(x)
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    numlist = get_user_input()
    average = calc_average_temperature(numlist)
    minmax = calc_min_max_temperature(numlist)
    median = int(calc_median_temperature(numlist))
    print(f"The average temperature is: {average} degrees celsius")
    print(f"The minimum and maximum temperature are: {minmax} degrees celsius")
    print(f"The median temperature is {median}")


if __name__ == "__main__":
    main()