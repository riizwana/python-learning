# I am going to get the user to put their input in
user_input = input()

# Now after assigning the variable I made to an actual function, it has something it needs to do which is
# getting the function to take an input when we prompt "user_input".
# Now I need to ensure whatever input I made to the terminal, even if its caps, we have to have it lowered.
# I made another variable called lowercase_input and that equals the user
# This is so that I can lowercase what the user inputs via the user_input.
lowercase_input = user_input

lowercase_input = user_input.lower()
# Lower() in documentation means anything printed within the variable input will be forced to be lowercased.
# I can attach the .lower() after the variable so that the variable input itself will be affected by that "command"

print(lowercase_input)
