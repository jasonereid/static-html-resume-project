# Resume static HTML file creation Python project
# Created by Jason Reid 11/1/2021
# don't forget to create an output.html file in your project folder before running the script.

print("This project takes input from the user to create a static resume webpage in HTML")
print("First, choose a page title. Your Name's Resume will work: ")
title = str(input())
print("Next, please input the heading at the top of the page. Most people use their name:")
heading = str(input())
print("Ok, let's add a paragraph about yourself. What are your goals, objectives, strengths, etc?")
paragraph1 = str(input())
print("Next, let's get your contact info.")
print("Your phone number: ")
phone1 = str(input())
print("Your email: ")
email1 = str(input())
print("Now, let's list your skills in bullet points. How many skills do you have?")
skillNumber = int(input())
skillsList = []
print("Ok, you have " + str(skillNumber) + " of skills. Please enter your skills: ")
# creating the skill list
for i in range(0, skillNumber):
    skillInput = str(input())

    skillsList.append(skillInput) # adding new skills to end of list

print("Your skills: " + str(skillsList))

# convert the list to HTML
def convertList2HTML(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    return string

print(convertList2HTML)

# job 1
print("Ok let's get your recent job history. First, your latest job: ")
print("Your Position Title: ")
jobTitle1 = str(input())
print("Your Company Name: ")
companyName1 = str(input())
print("Years worked, in this format: 1999 - 2005")
yearsWorked1 = str(input())
print("One short sentence describing your job: ")
jobDescription1 = str(input())

# job 2
print("Job 2: ")
print("Your Position Title: ")
jobTitle2 = str(input())
print("Your Company Name: ")
companyName2 = str(input())
print("Years worked, in this format: 1999 - 2005")
yearsWorked2 = str(input())
print("One short sentence describing your job: ")
jobDescription2 = str(input())

# job 3
print("Job 3: ")
print("Your Position Title: ")
jobTitle3 = str(input())
print("Your Company Name: ")
companyName3 = str(input())
print("Years worked, in this format: 1999 - 2005")
yearsWorked3 = str(input())
print("One short sentence describing your job: ")
jobDescription3 = str(input())

# choose page colors

# choose page font

# get page text

# output to html file


text = '''
<!DOCTYPE html>
<html>
<head>
<title> ''' + title + '''</title>
</head>
    <body>
        <h1> ''' + heading + '''</h1>
        <p>''' + paragraph1 + '''</p>
        <h3>Contact Information</h3>
        <p> Phone: ''' + phone1 + ''' Email: ''' + email1 + '''</p>
        <h3>Skills</h3>
        ''' + convertList2HTML(skillsList) + '''
        <h3>Work History</h3>
        <h4> ''' + jobTitle1 + ''' </h4>
        <p> ''' + companyName1 + ''' ''' + yearsWorked1 + ''' <br>
        ''' + jobDescription1 + ''' </p>
        <h4> ''' + jobTitle2 + ''' </h4>
        <p> ''' + companyName2 + ''' ''' + yearsWorked2 + ''' <br>
        ''' + jobDescription2 + ''' </p>
        <h4> ''' + jobTitle3 + ''' </h4>
        <p> ''' + companyName3 + ''' ''' + yearsWorked3 + ''' <br>
        ''' + jobDescription3 + ''' </p>
    
    </body>
</html>
'''

file = open("output.html","w")
file.write(text)
file.close()