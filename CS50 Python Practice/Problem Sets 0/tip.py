def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # I can convert the "dollars" above into "dollarfloat" after creating the variable
    # Dollarfloat would be associated with the "d" and "d" is defined with dollars_to_float
    dollarfloat = d.replace("$", "")
    # It got complicated for me here on how to return, but when returning floats, "float" has to be specified with the particular variable within brackets
    return float (dollarfloat)


def percent_to_float(p):
    # Similar process here, I did the same exact thing but with percent
    percentfloat = p.replace("%", "")
    # Only difference is that percentage is replaced with the intention of having it as an integar too
    # So a % is divided by 100 after we specified the float to return as well as ensuring that int is divided by 100
    return float (percentfloat) / 100


main()
