import numpy as np 

def function(x):

	c4 = x
	p5 = x
	paths = []
	try:
		if c4 > 2:
			x = 1-c4
			paths.append(1)
		else:
			p5 = p5*x
			p5 = 2/p5
			x = 2-4
			paths.append(2)
		if c4 >= 2:
			c4 = 9-p5
			x = 2-x
			paths.append(3)
		else:
			p5 = c4-p5
			x = 6*1
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		p5 = c4**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))