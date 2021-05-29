import numpy as np 

def function(x):

	w1 = 3
	c9 = x
	paths = []
	try:
		if w1 < 0:
			c9 = 7+x
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x >= 9:
			w1 = 7/w1
			x = x*w1
			paths.append(3)
		else:
			w1 = 8+x
			c9 = 2+c9
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))