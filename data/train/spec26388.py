import numpy as np 

def function(x):

	c4 = x
	w6 = 7
	paths = []
	try:
		if c4 <= 3:
			w6 = c4/w6
			x = x/c4
			paths.append(1)
		else:
			c4 = 3*w6
			c4 = c4+c4
			paths.append(2)
		if x <= 3:
			w6 = 8*w6
			c4 = c4*c4
			x = x*w6
			paths.append(3)
		else:
			w6 = w6/x
			w6 = 7-9
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))