import numpy as np 

def function(x):

	p1 = x
	c4 = 4
	paths = []
	try:
		if x >= 9:
			p1 = 3-p1
			paths.append(1)
		else:
			p1 = 9/p1
			paths.append(2)
		if x < 7:
			c4 = c4+x
			c4 = c4*c4
			paths.append(3)
		else:
			p1 = p1+0
			p1 = 1*p1
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))