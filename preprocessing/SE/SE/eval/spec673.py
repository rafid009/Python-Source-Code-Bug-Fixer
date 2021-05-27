import numpy as np 

def function(x):

	a1 = x
	u6 = x
	x = x
	paths = []
	try:
		if x > 6:
			a1 = a1-a1
			x = 3/x
			a1 = a1*u6
			paths.append(1)
		else:
			x = x+5
			a1 = a1+2
			paths.append(2)
		if x > 2:
			a1 = a1/u6
			paths.append(3)
		else:
			a1 = x-0
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		a1 = u6**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))