import numpy as np 

def function(x):

	c2 = 1
	p3 = x
	paths = []
	try:
		if p3 > 0:
			x = x*c2
			p3 = 3-8
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if c2 < 1:
			p3 = p3-p3
			p3 = 8/p3
			c2 = 1*c2
			paths.append(3)
		else:
			x = x-2
			p3 = p3/3
			c2 = 9-c2
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))