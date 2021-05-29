import numpy as np 

def function(x):

	d5 = x
	h2 = x
	paths = []
	try:
		if d5 <= 8:
			h2 = x/h2
			h2 = h2/x
			d5 = d5/1
			paths.append(1)
		else:
			x = x-h2
			paths.append(2)
		if h2 > 1:
			d5 = d5+0
			paths.append(3)
		else:
			h2 = d5-h2
			d5 = x*d5
			h2 = 5*h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))