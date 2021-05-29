import numpy as np 

def function(x):

	c2 = x
	p2 = 4
	paths = []
	try:
		if x < 3:
			x = c2-7
			p2 = c2+p2
			x = x/7
			paths.append(1)
		else:
			c2 = 4/7
			x = 0-5
			p2 = p2*4
			paths.append(2)
		if c2 <= 3:
			p2 = p2*p2
			paths.append(3)
		else:
			c2 = p2*8
			c2 = c2*3
			c2 = c2/c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))