"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - BIEBER STRUGGLES IN SINGAPORE **

Make employee-list into a dictionary as below, remove last entry (gender)
'M' or 'F' from each employee, as company-policy no longer allows.

# format: {'Name, emp.#, base-pay, gender'}
employees_old = 'Joe,1,110,M*Sue,2,120,F*Bo,3,95,M*Li,4,90,F*Ty,5,80,M*Vi,6,86,F'

# new employee-dictionary:
employees_d : {'Joe':'1,110','Sue':'2,120','Bo':'3,95','Li':'4,90','Ty':'5,80','Vi':'6,86'}

# bonus: to further impress client, convert to dictionary with list of
# numbers as below:
employees_d2: {'Joe':[1,110],'Sue':[2,120],'Bo':[3,95],'Li':[4,90],'Ty':[5,80],'Vi':[6,86]}
"""
from typing import Dict

employees_old = 'Joe,1,110,M*Sue,2,120,F*Bo,3,95,M*Li,4,90,F*Ty,5,80,M*Vi,6,86,F'


def clean_up(
    data: str,
    outer: str = "*",
    inner: str = ",",
) -> Dict[str, str]:
    return {
        name: list(map(int, values)) for name, *values
        in [line.split(inner)[:-1] for line in data.split(outer)]
    }


def main():
    employees_new = clean_up(employees_old)
    print(employees_new)


if __name__ == "__main__":
    main()
