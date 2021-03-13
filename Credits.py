import random

# Set interest rate to 0
interest = 0

# transactions generator
trans = [random.randrange(1, 1000) for _ in range(100)]

# geting the last 50 actual transactions
first_actuals = trans[0:50:]
last_actuals = trans[50::]

# defining the class "credits"


class Credit():
    def __init__(self, interest, first_actuals, last_actuals, trans):
        self.interest = interest
        self.trans = trans
        self.first_actuals = first_actuals
        self.last_actuals = last_actuals

#  creating a max and min formula as alternative
    def fiscal_eliminator(self):

        # Finding the total sum of the first and second 50 transactions
        total_value1 = 0
        for i in first_actuals:
            i += 0
            total_value1 += i
        total_value2 = 0
        for i in last_actuals:
            i += 0
            total_value2 += i
        print(f'First 50 Total: {total_value1}')
        print(f'Second 50 Total:{total_value2}')

        # stablizing inflatiion and deflation
        if total_value2 == total_value1:
            print('stable')
        elif total_value2 > total_value1:
            diff = total_value2 - total_value1
            self.interest = diff/total_value1
            print(f'New Interest:{self.interest}, more money supply')
        elif total_value1 > total_value2:
            diff = total_value1 - total_value2
            self.interest = - diff/total_value2
            print(f'New Interest:{self.interest},  take money out')

        total = 0
        for i in self.trans:
            i += 0
            total += i
            total_plusint = total + (total * self.interest)
        return (f'Total = {total}, New Interest = {self.interest}, Total w/ Int = {total_plusint}')

    # created an average to sustitute rise/run

        def averages_val(self):
            total = 0
            for i in self.trans:
                i += 1
                total += i
            averages = total/len(self.trans)  # using an average as the slope
            return averages


# giving an interest to all parties in a transaction
test0 = Credit(interest, trans, first_actuals, last_actuals)
print(test0.fiscal_eliminator())
