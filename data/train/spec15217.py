import numpy as np 

def function(x):

	w9 = x
	c4 = x
	paths = []
	try:
		if w9 <= 6:
			x = x+0
			x = 4*2
			c4 = c4+c4
			paths.append(1)
		else:
			c4 = c4*w9
			c4 = 1*c4
			paths.append(2)
		if x < 9:
			x = 0-x
			w9 = w9-0
			c4 = c4*2
			paths.append(3)
		else:
			x = x+x
			x = w9+x
			c4 = c4*2
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))