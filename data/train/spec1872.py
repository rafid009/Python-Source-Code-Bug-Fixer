import numpy as np 

def function(x):

	c8 = x
	p4 = 3
	paths = []
	try:
		if p4 >= 7:
			p4 = 5-p4
			c8 = x/c8
			c8 = c8+x
			paths.append(1)
		else:
			c8 = c8-3
			p4 = x+x
			c8 = p4+4
			paths.append(2)
		if x > 1:
			c8 = c8+c8
			c8 = x*c8
			c8 = 0-9
			paths.append(3)
		else:
			c8 = c8/9
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))