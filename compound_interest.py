
print 'This is a compound interest calculator, assuming a loan of $10,000 at a rate of 8%.'

p = 10000
n = 12
r = .08
t = int(raw_input('How many years is this loan for?: '))

a = p * (((r / n) + 1) ** (n * t))

print 'The total amount is %.2f'%(a)
