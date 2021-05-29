import numpy as np 

def function(x):

	a5 = x
	c1 = 6
	paths = []
	try:
		if a5 < 4:
			a5 = c1*x
			paths.append(1)
		else:
			a5 = 2-4
			a5 = a5-6
			x = x+0
			paths.append(2)
		if c1 <= 9:
			x = a5+7
			x = 9*9
			x = 8-6
			paths.append(3)
		else:
			x = 8*x
			x = x-3
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))