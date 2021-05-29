import numpy as np 

def function(x):

	l3 = 8
	h5 = x
	paths = []
	try:
		if h5 > 3:
			l3 = l3/4
			x = 8*x
			h5 = h5*1
			paths.append(1)
		else:
			x = 8/l3
			paths.append(2)
		if l3 > 3:
			h5 = 5*h5
			l3 = 6/l3
			h5 = 2-8
			paths.append(3)
		else:
			l3 = l3*l3
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))