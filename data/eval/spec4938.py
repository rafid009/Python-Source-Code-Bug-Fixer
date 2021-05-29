import numpy as np 

def function(x):

	a3 = x
	c2 = 6
	paths = []
	try:
		if a3 >= 9:
			x = 4-c2
			paths.append(1)
		else:
			x = a3*x
			paths.append(2)
		if x <= 0:
			c2 = c2-4
			paths.append(3)
		else:
			x = x/7
			c2 = c2+1
			x = 7+c2
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))