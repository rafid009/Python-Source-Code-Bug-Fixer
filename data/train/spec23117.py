import numpy as np 

def function(x):

	w8 = 3
	c5 = x
	paths = []
	try:
		if c5 > 5:
			w8 = c5/c5
			paths.append(1)
		else:
			c5 = 1*c5
			c5 = x+c5
			paths.append(2)
		if w8 >= 8:
			w8 = w8*2
			paths.append(3)
		else:
			c5 = 8*c5
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