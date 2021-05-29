import numpy as np 

def function(x):

	a6 = 5
	u1 = 6
	paths = []
	try:
		if a6 <= 5:
			u1 = u1*u1
			u1 = 7+u1
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if u1 < 8:
			u1 = 6+u1
			x = x/x
			x = x*9
			paths.append(3)
		else:
			a6 = x/a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))