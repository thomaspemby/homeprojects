class Employee:
    def set_payment(self, hourscompleted):
        payment = 0
        float(hourscompleted)
        if hourscompleted >= 30:
            payment = hourscompleted * 15
        elif hourscompleted >= 15 and hourscompleted < 29:
            payment = hourscompleted * 12
        else:
            payment = hourscompleted * 9
        return payment


e = Employee()
hourscompleted = float(input("Please enter the amount of hours worked by the employee: "))
hourscalculated = e.set_payment(float(hourscompleted))
print(f"Ammount earnt: £{str(hourscalculated)}")