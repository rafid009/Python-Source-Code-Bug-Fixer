import numpy as np 

def function(x):

	c4 = 6
	p1 = x
	paths = []
	try:
		if c4 >= 1:
			p1 = p1+7
			p1 = p1+c4
			paths.append(1)
		else:
			x = 5*x
			x = 7/9
			c4 = 1+c4
			paths.append(2)
		if p1 > 0:
			p1 = 1*p1
			paths.append(3)
		else:
			x = 7*p1
			c4 = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))