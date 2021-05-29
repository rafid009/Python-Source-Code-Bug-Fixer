import numpy as np 

def function(x):

	h2 = x
	d2 = x
	paths = []
	try:
		if d2 < 1:
			d2 = d2*8
			x = x-5
			x = x/d2
			paths.append(1)
		else:
			x = x/5
			x = x-h2
			h2 = h2+7
			paths.append(2)
		if d2 > 3:
			x = 1/6
			h2 = 9-9
			h2 = 9-d2
			paths.append(3)
		else:
			d2 = d2*7
			h2 = h2/4
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))