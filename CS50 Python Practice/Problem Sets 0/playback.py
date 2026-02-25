# I need to get the input from the user

user_input = input()

# With the user input, I need to split whatever they have just said and I can use that variable too
# Looking into documentation, the "split" function is most likely, and it has a "sep=" that we need to make a distinction as to what the input could be separated with
# I don't think we need to use maxsplit right now.

splitwords = user_input.split()

# I called the split function now to the variable so now we need to let it know what it needs to split through the seperator
# We can return that through a print

print(*splitwords, sep="...")
# The asterik allows the passing of any number of objects from the input. It could be a large sentence.
# When I have done it without the asterik, it does not split it properly and with commas and square brackets.
