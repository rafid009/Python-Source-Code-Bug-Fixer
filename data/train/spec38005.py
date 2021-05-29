import numpy as np 

def function(x):

	w2 = 9
	c6 = x
	paths = []
	try:
		if c6 < 9:
			x = 0/w2
			x = 3+x
			paths.append(1)
		else:
			w2 = 7-w2
			paths.append(2)
		if w2 >= 4:
			w2 = 4/c6
			x = 4/x
			paths.append(3)
		else:
			w2 = w2*x
			c6 = c6/4
			c6 = x+9
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))