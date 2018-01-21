# Birthday Months


from collections import Counter
import json


def create_months():
    return {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }


if __name__ == '__main__':
    months, birthday_holder = create_months(), {}
    existing_months = []

    with open("data/birthdays.json") as f:
        birthday_holder = json.load(f)

    for k,v in birthday_holder.items():
        m_key = v.split("/")[0]
        existing_months.append(months[m_key])

    c = Counter(existing_months)

    print(c)
