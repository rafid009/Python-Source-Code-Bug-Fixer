import numpy as np 

def function(x):

	p1 = x
	c0 = 3
	paths = []
	try:
		if c0 <= 0:
			p1 = p1*1
			p1 = 5+p1
			paths.append(1)
		else:
			x = 8+x
			x = x-x
			paths.append(2)
		if c0 <= 5:
			c0 = c0*c0
			c0 = 9+p1
			paths.append(3)
		else:
			x = x+4
			x = x+9
			c0 = 4*7
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		p1 = c0**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))