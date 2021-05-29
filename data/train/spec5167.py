import numpy as np 

def function(x):

	w1 = 2
	c3 = x
	paths = []
	try:
		if w1 <= 5:
			x = 7+x
			paths.append(1)
		else:
			c3 = w1-c3
			w1 = w1+x
			paths.append(2)
		if w1 < 0:
			c3 = c3/2
			x = 7+x
			paths.append(3)
		else:
			c3 = c3+c3
			x = c3/x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))