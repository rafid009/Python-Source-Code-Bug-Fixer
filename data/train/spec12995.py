import numpy as np 

def function(x):

	c3 = 6
	l3 = x
	paths = []
	try:
		if c3 >= 5:
			l3 = x+x
			c3 = 4*c3
			paths.append(1)
		else:
			c3 = 3/l3
			x = x+9
			c3 = 7*3
			paths.append(2)
		if l3 >= 4:
			c3 = 0/c3
			paths.append(3)
		else:
			l3 = l3*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))