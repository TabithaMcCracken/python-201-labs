# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.
import os
first_secret = os.environ['ENVIRONMENT']
second_secret = os.environ['SECRET']

print(first_secret)
print(second_secret)