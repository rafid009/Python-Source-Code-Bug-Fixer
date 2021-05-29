import numpy as np 

def function(x):

	u2 = 4
	x7 = x
	paths = []
	try:
		if x < 9:
			u2 = 5*x
			x = x7*2
			paths.append(1)
		else:
			u2 = 3-u2
			u2 = 3*u2
			x = x*6
			paths.append(2)
		if u2 > 7:
			u2 = u2*1
			paths.append(3)
		else:
			u2 = u2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))