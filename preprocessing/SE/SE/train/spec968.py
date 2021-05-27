import numpy as np 

def function(x):

	q9 = x
	u0 = x
	paths = []
	try:
		if u0 > 7:
			q9 = 6+q9
			x = x+6
			paths.append(1)
		else:
			u0 = 5-x
			paths.append(2)
		if x > 4:
			q9 = 1/x
			u0 = u0+q9
			q9 = 7*q9
			paths.append(3)
		else:
			u0 = 7-9
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))