import numpy as np 

def function(x):

	a5 = 5
	h5 = x
	paths = []
	try:
		if h5 < 4:
			h5 = a5/a5
			a5 = a5*1
			paths.append(1)
		else:
			x = 1+x
			x = x*0
			paths.append(2)
		if x < 9:
			h5 = x-h5
			h5 = h5/a5
			a5 = a5*7
			paths.append(3)
		else:
			x = x+h5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))