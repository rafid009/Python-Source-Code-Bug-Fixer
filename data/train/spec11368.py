import numpy as np 

def function(x):

	h3 = x
	t2 = 7
	paths = []
	try:
		if x <= 1:
			x = x+9
			h3 = h3*x
			paths.append(1)
		else:
			t2 = 3+x
			x = x*4
			paths.append(2)
		if h3 >= 1:
			h3 = h3*5
			paths.append(3)
		else:
			t2 = t2-8
			x = x-0
			t2 = t2*x
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