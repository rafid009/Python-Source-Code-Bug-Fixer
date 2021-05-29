import numpy as np 

def function(x):

	f3 = 2
	c5 = 9
	paths = []
	try:
		if x <= 9:
			f3 = f3*5
			f3 = f3*7
			c5 = c5*x
			paths.append(1)
		else:
			f3 = x/f3
			paths.append(2)
		if x >= 4:
			c5 = x/c5
			c5 = 3/f3
			paths.append(3)
		else:
			f3 = f3-6
			f3 = 5*x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))