import numpy as np 

def function(x):

	c5 = x
	p7 = 6
	x = 7
	paths = []
	try:
		if x >= 5:
			x = x-9
			p7 = p7+3
			paths.append(1)
		else:
			p7 = p7-x
			p7 = p7/5
			paths.append(2)
		if c5 > 0:
			p7 = 2-p7
			c5 = c5-5
			p7 = 3*p7
			paths.append(3)
		else:
			x = 8*5
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		p7 = c5**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))