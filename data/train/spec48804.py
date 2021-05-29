import numpy as np 

def function(x):

	h2 = 5
	d9 = x
	paths = []
	try:
		if h2 < 4:
			d9 = 1+d9
			h2 = h2/8
			paths.append(1)
		else:
			d9 = d9*d9
			x = x-1
			x = 1-x
			paths.append(2)
		if d9 > 8:
			h2 = 2+h2
			h2 = d9*h2
			h2 = x*h2
			paths.append(3)
		else:
			d9 = d9*3
			h2 = 2-h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))