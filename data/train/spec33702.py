import numpy as np 

def function(x):

	c2 = x
	w2 = x
	paths = []
	try:
		if x <= 8:
			w2 = w2-5
			c2 = 0*c2
			w2 = w2+x
			paths.append(1)
		else:
			c2 = 5+c2
			w2 = x/x
			w2 = w2*x
			paths.append(2)
		if w2 >= 9:
			x = 3-9
			x = x*7
			w2 = w2*c2
			paths.append(3)
		else:
			x = x-c2
			x = 5-x
			w2 = w2+c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))