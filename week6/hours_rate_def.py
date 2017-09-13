def computepay(h,r):
    pay = h * (r * 1.5) - 210
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

if h <= 40:
    p = h * r
else:
	p = computepay(h,r)

print(p)
