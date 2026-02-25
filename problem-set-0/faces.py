# Let's ask for the user's input
def main():
    # Now we can ask the user:
    user_input = input()
    # If the user uses :) or :(, I want it to be converted so now we have to make a function called convert
    converted = convert(user_input)
    # We have the convert function now and situated the user_input
    # Now I have to ensure it gets printed out
    print(f"{converted}")
    # Formatting is used and placed in front before the dialogue to tell python to format this string to input variable


def convert(line):
    # This function will tell the program what exactly we need to convert
    # Line essentially is the reference.
    # Reading the doc, this is most likely the best to use: str.replace(old, new, /, count=-1)
    return line.replace(":)" , "🙂").replace(":(" , "🙁")
# Following the str.replace(), we are converting :) "old" and with the emoji as "new".


main()
# And we call the program to run
