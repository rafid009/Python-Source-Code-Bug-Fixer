import numpy as np 

def function(x):

	q4 = x
	u0 = 8
	paths = []
	try:
		if u0 >= 7:
			q4 = q4*2
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if x < 5:
			u0 = q4*q4
			u0 = 6+u0
			paths.append(3)
		else:
			u0 = u0+6
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))