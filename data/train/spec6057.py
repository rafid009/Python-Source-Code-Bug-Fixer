import numpy as np 

def function(x):

	c4 = x
	p5 = x
	paths = []
	try:
		if c4 >= 3:
			x = x+0
			c4 = x-c4
			paths.append(1)
		else:
			c4 = 9+c4
			paths.append(2)
		if x >= 8:
			p5 = 4-c4
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		p5 = p5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))