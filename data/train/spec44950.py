import numpy as np 

def function(x):

	p6 = 1
	c3 = 9
	paths = []
	try:
		if x > 2:
			x = 3+x
			paths.append(1)
		else:
			p6 = 1-7
			c3 = c3+6
			p6 = p6*5
			paths.append(2)
		if c3 > 7:
			c3 = x-8
			paths.append(3)
		else:
			p6 = p6+7
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))