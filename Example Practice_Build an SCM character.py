#In this lab, you will practice the basics of Python by building a small app that creates a character for an SCM adventure
#OBJECTIVE: Fulfill the user stories below and get all the tests to pass to complete the lab
#User stories:
#1. You should have a function named create_SCM_character
#2. The function should accept, in order, a character name followed by three times: pickingtime, packingtime and shippingtime
#3. The character name should be validated: 
    #i. If the character name is not a string, the function should return "The character name should be a string"
    #ii. If the character name is longer than 10 characters, the function should return "The character name is too long"
    #iii. If the character name contains spaces, the function should return "The character name should not contain spaces"
#4. The times should also be validated:
    #i. If one or more times are not integers, the function should return "All times should be integers"
    #ii. If one or more times are less than 1, the function should return "All times should be no less than 1"
    #iii. If one or more times are more than 4, the function should return "All times should be no less than 4"
    #iv. If the sum of all the times is different than 7, the function should return "The character should start with 7 points"
#5. If all values pass the verification, the function should return a string with four lines:
    #i. The first line should contain the character name
    #ii. lines 2-4 should start with the stat abbreviation, STR, INT or CHA, then a space, and then a number of full dots equal to the value of the stat, and a number of the empty dots to reach 10.

#---------------------------------------- TESTS ------------------------------------------------------------
## 1. You should have a function named create_SCM_character
def create_SCM_character(name, pickingtime, packingtime, shippingtime):
## 2. When create_SCM_character is called with a first argument that is not a string it should return "The character name should be a string"
    if not isinstance(name, str):
        return 'The character name should be a string'
## 3. When create_SCM_character is called with a first argument that is longer than 10 characters it should return "The character name is too long"
    if len(name) > 10:
        return 'The character name is too long'
    times = [pickingtime, packingtime, shippingtime]
## 4. When create_SCM_character is called with a first argument that contains a space it should return "The character name should not contain spaces"
    if " " in name:
        return "The character name should not contain spaces"
## 5. When create_SCM_character is called with second, third, and fourth argument that is not integer it should return "All times should be integers"
    if not all(isinstance(time, int) for time in times):
        return 'All times should be integers'
## 6. When create_SCM_character is called with second, third, and fourth argument that is lower than 1 it should return "All times should be no less than 1"
    if any(time < 1 for time in times):
        return 'All times should be no less than 1'
## 7. When create_SCM_character is called with second, third, and fourth argument that is higher than 4 it should return "All times should be no more than 4"
    if any(time > 4 for time in times):
        return 'All times should be no more than 4'
## 8. When create_SCM_character is called with second, third, and fourth argument that do not sum to 7 it should return "The character should start with 7 points"
    if sum(times) != 7:
        return 'The character should start with 7 points'
# 9. create_character("leadtime", 4, 2, 1) should return leadtime\nPIT ●●●●○○○○○○\nPKT ●●○○○○○○○○\nSPT ●○○○○○○○○○.
    full_dot = '●'
    empty_dot = '○'
    picking_full = full_dot * pickingtime
    picking_emp  = empty_dot * (10-pickingtime)
    packing_full = full_dot * packingtime
    packing_emp = empty_dot * (10-packingtime)
    shipping_full = full_dot * shippingtime
    shipping_emp = empty_dot * (10-shippingtime)
    return f'{name}\nPIT{picking_full}{picking_emp}\nPKT{packing_full}{packing_emp}\nSPT{shipping_full}{shipping_emp}'
character = create_SCM_character("leadtime", 4, 2, 1)
