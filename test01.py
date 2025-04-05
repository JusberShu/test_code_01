# This is a test function


def Get_even_nbs():

    while True:
        number = int(input("Pls input an integer(must be no less than 1): "))
        x = 0
        if number > 1 or number == 1:
            for i in range(1, number):
                if i % 2 == 0:
                    x += i
                print(f"The even number is {x} 'number sequence {i}")

        else:
            print("The number should be integer, ie. no less than 1\n")
            print("Please try again.")


Get_even_nbs()
