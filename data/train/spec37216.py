import numpy as np 

def function(x):

	a8 = x
	c5 = x
	paths = []
	try:
		if a8 <= 7:
			a8 = 9/a8
			c5 = c5*1
			paths.append(1)
		else:
			x = x-2
			a8 = x*a8
			paths.append(2)
		if c5 > 3:
			x = x-7
			c5 = c5/a8
			paths.append(3)
		else:
			x = x+a8
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		a8 = c5**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))