"""
Name: <Madison Byrne>
<mean>.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work; however, I used the internet
"""
def main():
    #input the amount the number roads
    roads = eval(input("Enter the number of roads:"))
    #input total of number of cars
    vehicles = 0
    overall_average = 0
    average_vehicles = 0

    for n in range(roads):
        string = str(n +1)
        #input the amount of cars that travel each day
        days = eval(input("Enter the number of days that the road" + string + " was surveyed: "))#input a string within eval statement
        total = 0

        for i in range(days):
            #input your string and have a similar format to first loop
            string_2 = str(i + 1)
            cars = eval(input("Enter the number of cars traveled" +string_2+ "on this day:"))#have to input a string
            total += cars

            overall_average = total / days
            vehicles += cars
            average_vehicles = vehicles / roads

        print("average amount of vehicles that traveled: ", round(overall_average,2))
    print("Total number of vehicles that traveled on all roads: ", round(vehicles,2))
    print("Average number of vehicles that traveled on each road:", round(average_vehicles))
    #print statements

if __name__=='__main__':
    main()

