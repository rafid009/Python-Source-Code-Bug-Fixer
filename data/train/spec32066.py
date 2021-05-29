import numpy as np 

def function(x):

	c1 = x
	p3 = 9
	x = 9
	paths = []
	try:
		if c1 >= 3:
			c1 = c1/c1
			c1 = 7/x
			p3 = x+6
			paths.append(1)
		else:
			p3 = p3+4
			p3 = 8+0
			paths.append(2)
		if x >= 4:
			p3 = 0*1
			x = 3+x
			x = 3+c1
			paths.append(3)
		else:
			c1 = 8+7
			x = 7+x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))