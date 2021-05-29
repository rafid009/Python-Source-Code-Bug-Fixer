import numpy as np 

def function(x):

	c9 = x
	a3 = 9
	paths = []
	try:
		if c9 <= 5:
			a3 = 1+a3
			c9 = 5/c9
			paths.append(1)
		else:
			a3 = a3*2
			paths.append(2)
		if x <= 3:
			c9 = c9-0
			paths.append(3)
		else:
			a3 = 0*x
			a3 = a3-4
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		a3 = c9**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))