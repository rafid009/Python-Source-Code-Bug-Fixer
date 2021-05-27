import numpy as np 

def function(x):

	p4 = x
	c6 = x
	paths = []
	try:
		if c6 < 6:
			c6 = c6-9
			c6 = c6+9
			paths.append(1)
		else:
			c6 = p4-c6
			paths.append(2)
		if p4 > 7:
			c6 = c6-x
			p4 = x+p4
			paths.append(3)
		else:
			x = 1*0
			x = x-7
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))