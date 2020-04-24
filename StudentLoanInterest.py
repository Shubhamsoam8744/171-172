# Develop a Python program to compare loans. The program should ask the user for two inputs. First, ask for the total amount of principle borrowed. Next, ask for the number of years on the loan. Assume all loans make 12 payments per year.
#
# Your program will then compute all the following values for three different types of loans.
#
# When printing values, you can round by using round(val,2).
#
# Principle
# Interest Rate
# Years
# Monthly Payment
# Total Paid on Loan
# Total Interest Paid
# Additional Fees Paid
# Total Costs Over Principle
# Compare the Following three types of loans.
#
# Subsidized Federal Direct
# Interest: 3.4%
# Fee: 1.051%
# Unsubsidized Federal Direct
# Interest: 6.8%
# Fee: 1.051%
# Unsubsidized PLUS Loan
# Interest: 7.9%
# Fee: 4.204%


def displayInfo(loanPrinciple, loanInterest, yearsOfLoan, feePercent, paymentInYear = 12):
    monthlyPayments = (loanPrinciple * loanInterest) / (paymentInYear * (1 - (1 + loanInterest / paymentInYear) ** (-yearsOfLoan * paymentInYear)))
    totalPaid = monthlyPayments * paymentInYear * yearsOfLoan
    totalInt = totalPaid - loanP
    fee = feePercent * loanP
    print('Principle:', loanP)
    print('Interest Rate:', round(loanInterest * 100, 1))
    print('Years:', yearsOfLoan)
    print('Monthly Payment', round(monthlyPayments, 2))
    print('Total Paid on Loan:', round(totalPaid, 2))
    print('Total Interest Paid:', round(totalInt, 2))
    print('Additional Fees Paid:', round(fee, 2))
    print('Total Costs Over Principle:', round(totalInt + fee, 2))

print('Welcome to the Student Loan Calculator')
print('Enter the amount of the loan in dollars with (no commas):')
loanP = int(input())
print('Enter the number of years the loan will be for:')
years = int(input())

print('------------------------------')
print('Subsidized Federal Direct Loan')
displayInfo(loanP, 0.034, years, 0.01051)

print('------------------------------')
NewPrinciple = loanP * (1+0.068 * 4.25)
print('Unsubsidized Federal Direct Loan')
displayInfo(NewPrinciple, 0.068, years, 0.01051)

print('------------------------------')
NewPrinciple = loanP * (1 + 0.079 * 4.25)
print('Federal Plus Loan')
displayInfo(NewPrinciple, 0.079, years, 0.04204)