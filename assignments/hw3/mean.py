
"""
Name: <Madison Byrne>
<mean>.py

Problem: create a program that represents three different ways of calculating mean

Certification of Authenticity:
I certify that this assignment is entirely my own work; however, I used the
"""
import math

def main():
    def the_mean():
        # put the rms, harmonic and geometric in the same loop and write their code together
        n_values = eval(input("enter the values: "))
        total_value = 0  # adding to 0 for summation
        values = 0
        multiply_the_result = 1  # for the geometric loop

        for numbers in range(n_values): #start your loop from this
            numbers = eval(input("enter the values for your n value: "))
            total_value = total_value + numbers**2 #for harmonic
            values = values + 1/numbers
            multiply_the_result = multiply_the_result * numbers #multiply your product with your n value


        #set it up my output of the assignment
        rms = math.sqrt(total_value/n_values) #rms
        harmonic_mean = (n_values/ values) #for the harmonic mean
        geometric_mean = (multiply_the_result) ** (1/n_values) #equation for the geometric

        print(round(rms, 3))
        print(round(harmonic_mean,3))
        print(round(geometric_mean,3))

    the_mean()

if __name__ == '__main__':
    main()
