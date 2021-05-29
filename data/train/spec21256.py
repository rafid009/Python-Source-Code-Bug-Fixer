import numpy as np 

def function(x):

	c5 = x
	n0 = 3
	paths = []
	try:
		if c5 < 4:
			x = x/9
			n0 = 2/n0
			paths.append(1)
		else:
			c5 = 0-1
			paths.append(2)
		if n0 >= 8:
			c5 = n0+9
			x = x/4
			paths.append(3)
		else:
			n0 = 2/2
			n0 = n0*0
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))