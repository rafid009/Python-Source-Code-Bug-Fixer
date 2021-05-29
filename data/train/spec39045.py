import numpy as np 

def function(x):

	h5 = x
	p9 = x
	paths = []
	try:
		if h5 <= 5:
			h5 = h5*p9
			h5 = p9*7
			paths.append(1)
		else:
			p9 = 7-1
			h5 = p9-h5
			paths.append(2)
		if h5 > 0:
			x = x*h5
			paths.append(3)
		else:
			h5 = 3/h5
			h5 = h5-6
			x = x*3
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		p9 = h5**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))