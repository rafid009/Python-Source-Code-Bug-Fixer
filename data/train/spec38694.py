import numpy as np 

def function(x):

	u6 = x
	a7 = 1
	x = 7
	paths = []
	try:
		if a7 < 4:
			x = a7-2
			paths.append(1)
		else:
			x = 4*x
			x = x+5
			a7 = 1-a7
			paths.append(2)
		if x < 9:
			x = x-5
			paths.append(3)
		else:
			x = 0+x
			a7 = x*5
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))