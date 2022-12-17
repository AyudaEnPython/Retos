"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - BIEBER STRUGGLES IN SINGAPORE **

Client uses IP-phones for alot of work. phones double as logging system
for hours worked, and capture other data in phone_m.
system registers monthly values for {'employee number':'logged hours at work',
'number of calls', 'total call-time in minutes','# feedback rated 4+'}

Client needs to calculate monthly employee wages = # hours worked * basepay
# employee_d1: {Name: [employee number, base pay/hour]}

employees_d1 = {'Joe': [1, 110], 'Sue': [2, 120], 'Bo': [3, 95],
'Li': [4, 90],'Ty': [5, 80], 'Vi': [6, 86]}

phone_m = {1:[180,1200,4783,223],2:[175,1213,4565,275],3:[155,1008,4145,180],
4:[160,1005,4315,138],5:[185,1265,6200,264],6:[160,1052,4532,184]}

# output should be a printed list, like
"Joe's monthly pay is 19 800 copper"
"Sue's monthly pay is 21 000 copper"
"Bo's monthly pay is 14 725 copper"
"Li's monthly pay is 14 400 copper"
"Ty's monthly pay is 14 800 copper"
"Vi's monthly pay is 13 760 copper"

# bonus:
# client would love if bonus of 1500 copper can be added for 1100+ calls
"""
from typing import Dict, List, Union

employees_d1 = {
    'Joe': [1, 110],
    'Sue': [2, 120],
    'Bo': [3, 95],
    'Li': [4, 90],
    'Ty': [5, 80], 
    'Vi': [6, 86],
}
phone_m = {
    1: [180, 1200, 4783, 223],
    2: [175, 1213, 4565, 275],
    3: [155, 1008, 4145, 180],
    4: [160, 1005, 4315, 138],
    5: [185, 1265, 6200, 264],
    6: [160, 1052, 4532, 184],
}


def _calculate(base_payment: int, info: List[int]):
    bonus = 1500 if info[1] > 1100 else 0
    return base_payment * info[0] + bonus


def payroll(
    data: Dict[str, List[int]],
    record: Dict[int, List[int]],
) -> List[List[Union[str, int]]]:
    return [
        [name, _calculate(base_p, record[id_])]
        for name, (id_, base_p) in data.items()
    ]


def show(wages: List[List[Union[str, int]]]) -> None:
    for name, wage in wages:
        print(f"{name}'s monthly pay is {wage} copper")


def main():
    wages = payroll(employees_d1, phone_m)
    show(wages)


if __name__ == "__main__":
    main()
