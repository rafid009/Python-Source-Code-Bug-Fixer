import numpy as np 

def function(x):

	x4 = 5
	a2 = 9
	paths = []
	try:
		if x <= 1:
			a2 = x4+a2
			a2 = a2/x4
			x4 = x4-7
			paths.append(1)
		else:
			x4 = 9/x4
			a2 = x*6
			a2 = a2/7
			paths.append(2)
		if a2 < 9:
			a2 = 6-9
			paths.append(3)
		else:
			a2 = a2-a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))