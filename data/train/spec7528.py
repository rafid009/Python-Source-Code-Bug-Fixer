import numpy as np 

def function(x):

	u2 = 3
	a5 = 8
	paths = []
	try:
		if u2 >= 4:
			a5 = x-a5
			a5 = a5/a5
			u2 = a5*u2
			paths.append(1)
		else:
			x = 3/x
			a5 = a5/2
			paths.append(2)
		if a5 <= 4:
			x = x*u2
			a5 = 9*a5
			paths.append(3)
		else:
			u2 = 8+1
			u2 = u2+u2
			u2 = 3/u2
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