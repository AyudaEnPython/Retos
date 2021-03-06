"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - BUG IN REGISTRATION **

Your user registration system had a bug, which got all the names
backwards. Write code to print names in proper format, before users
notice the problem.

wrong_names = ['Yrret ,Maharg, Nhoj,Yrret, Leahcim ,Cire']

# output:
'Correct names are: Eric, Michael, Terry, John, Graham, Terry'

# bonus:
- Also save the names in a proper list variable.
"""

wrong_names = ['Yrret ,Maharg, Nhoj,Yrret, Leahcim ,Cire']


def fix_bug(names):
    return [
        name.strip().lower()[::-1].title()
        for name in names[0].split(',')
    ][::-1]


print('Correct names are: ' + ', '.join(fix_bug(wrong_names)))
