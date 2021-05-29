import numpy as np 

def function(x):

	w2 = 5
	c0 = 9
	x = x
	paths = []
	try:
		if c0 < 8:
			c0 = x+c0
			paths.append(1)
		else:
			w2 = w2-x
			paths.append(2)
		if c0 < 4:
			x = c0/1
			w2 = 5*w2
			paths.append(3)
		else:
			c0 = 0-c0
			c0 = x/9
			c0 = c0/4
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))