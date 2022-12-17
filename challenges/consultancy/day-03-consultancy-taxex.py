"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - BIEBER STRUGGLES IN SINGAPORE **

Company must change payment practice, paying preliminary taxes direct
to state. Employees get paid net sum after taxes. Code monthly payslips!
wages = # hrs worked * basepay + 1500 bonus if employee makes > 1100 calls

Tax system is progressive paying 30% base rate on all income and 50% on
monthly income above 16 700 copper.
Example:
income 18500: 16700*0.3 + 1800*0.5 => 5010 + 900 = 5910 copper.
Average tax rate = 31.9%

# employee_d1: {Name: [employee number, base pay/hour]}
employees_d1 = {'Joe': [1, 110], 'Sue': [2, 120], 'Bo': [3, 95],
'Li': [4, 90],'Ty': [5, 80], 'Vi': [6, 86]}

# pnome_m: {'employee number': ['logged hours at work', 'numbers of call',
'total call-time in minutes', '# feedback rated 4+']}
phone_m = {1:[180,1200,4783,223],2:[175,1213,4565,275],3:[155,1008,4145,180],
4:[160,1005,4315,138],5:[185,1265,6200,264],6:[160,1052,4532,184]}

# output should be a printed list, like (bonus: make categories align as below)
"Joe's monthly after tax pay: 13 990 Gross: 21 300 tax: 7 310 Tax rate: 34.3%"
"Sue's monthly after tax pay: 14 590 Gross: 22 500 tax: 7 910 Tax rate: 35.2%"
"Bo's  monthly after tax pay: 10 308 Gross: 14 725 tax: 4 417 Tax rate: 30.0%"
"Li's  monthly after tax pay: 10 080 Gross: 14 400 tax: 4 320 Tax rate: 30.0%"
"Ty's  monthly after tax pay: 11 410 Gross: 16 300 tax: 4 890 Tax rate: 30.0%"
"Vi's  monthly after tax pay:  9 632 Gross: 13 760 tax: 4 128 Tax rate: 30.0%"
"""
from tkinter import W
from typing import Dict, List, Tuple, Union

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


def apply_tax(wage: int, limit: int = 16700) -> Tuple[int, float, float]:
    if wage > limit:
        after_tax = limit * 0.3 + (wage - limit) * 0.5
        return wage, after_tax, round(after_tax/wage * 100, 1)
    return wage, wage * 0.3, 30


def _calculate(base_payment: int, info: List[int]):
    bonus = 1500 if info[1] > 1100 else 0
    return base_payment * info[0] + bonus


def payroll(
    data: Dict[str, List[int]],
    record: Dict[int, List[int]],
) -> List[List[Union[str, int]]]:
    return [
        [name, apply_tax(_calculate(base_p, record[id_]))]
        for name, (id_, base_p) in data.items()
    ]


def show(wages: List[List[Union[str, int]]]) -> None:
    for name, (gross, tax, rate) in wages:
        after = round(gross - tax)
        name += "'s"
        print(
            f"{name:<5} {'monthly after tax pay: ':>23}{after:>6,} "
            f"| Gross: {gross:,d} "
            f"| Tax: {round(tax):>5,} "
            f"| Tax rate: {rate:.1f}%".replace(",", " ")
        )


def main():
    wages = payroll(employees_d1, phone_m)
    show(wages)


if __name__ == "__main__":
    main()
