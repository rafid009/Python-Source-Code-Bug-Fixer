import numpy as np 

def function(x):

	q9 = 6
	r0 = 1
	paths = []
	try:
		if x > 5:
			q9 = q9*8
			x = 7-0
			paths.append(1)
		else:
			r0 = 8*q9
			r0 = 7*7
			r0 = x*9
			paths.append(2)
		if x <= 9:
			r0 = r0*8
			x = x+r0
			paths.append(3)
		else:
			r0 = x-r0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))