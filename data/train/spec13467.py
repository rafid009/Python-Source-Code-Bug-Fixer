import numpy as np 

def function(x):

	p5 = x
	c5 = x
	paths = []
	try:
		if p5 > 5:
			x = 8-9
			p5 = 1+p5
			p5 = p5/4
			paths.append(1)
		else:
			p5 = p5-4
			paths.append(2)
		if c5 >= 9:
			c5 = 6-p5
			c5 = c5*3
			x = 3/8
			paths.append(3)
		else:
			p5 = p5-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))