import numpy as np 

def function(x):

	p5 = 3
	c1 = x
	paths = []
	try:
		if c1 <= 5:
			p5 = p5/1
			p5 = p5*x
			paths.append(1)
		else:
			x = x*3
			p5 = 2+4
			x = x/c1
			paths.append(2)
		if c1 >= 5:
			c1 = 3*c1
			x = x-7
			c1 = 2+c1
			paths.append(3)
		else:
			c1 = x-0
			x = 7+5
			c1 = p5-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))