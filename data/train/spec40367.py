import numpy as np 

def function(x):

	a2 = x
	u6 = x
	paths = []
	try:
		if u6 < 7:
			u6 = u6+u6
			u6 = 0-x
			paths.append(1)
		else:
			a2 = 1-1
			a2 = u6+6
			paths.append(2)
		if a2 >= 0:
			x = 8+x
			a2 = 6/a2
			paths.append(3)
		else:
			a2 = 4*a2
			a2 = a2/u6
			a2 = 8*a2
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		a2 = u6**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))