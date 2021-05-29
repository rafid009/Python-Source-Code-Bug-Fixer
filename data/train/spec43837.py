import numpy as np 

def function(x):

	d8 = 9
	h2 = 8
	paths = []
	try:
		if x > 3:
			x = x/4
			x = h2*5
			paths.append(1)
		else:
			d8 = x*d8
			d8 = d8/7
			paths.append(2)
		if h2 <= 1:
			h2 = h2*x
			x = x+x
			paths.append(3)
		else:
			h2 = h2*x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))