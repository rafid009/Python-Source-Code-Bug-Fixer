import numpy as np 

def function(x):

	w9 = 9
	c2 = 7
	paths = []
	try:
		if x < 9:
			c2 = 8*c2
			w9 = 4-w9
			w9 = 5*w9
			paths.append(1)
		else:
			x = 5+x
			c2 = 8*c2
			w9 = 2-7
			paths.append(2)
		if x >= 8:
			x = x*3
			paths.append(3)
		else:
			w9 = x-w9
			w9 = 4-5
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