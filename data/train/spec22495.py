import numpy as np 

def function(x):

	p9 = 3
	c2 = x
	x = x
	paths = []
	try:
		if x <= 6:
			x = x+8
			c2 = c2/2
			paths.append(1)
		else:
			c2 = c2/x
			p9 = p9+9
			paths.append(2)
		if c2 <= 5:
			p9 = c2*p9
			x = 4+1
			p9 = p9*4
			paths.append(3)
		else:
			x = x-6
			p9 = p9/5
			p9 = p9*4
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))