import numpy as np 

def function(x):

	d1 = x
	h2 = 7
	paths = []
	try:
		if x >= 5:
			x = 7-x
			x = h2+0
			paths.append(1)
		else:
			h2 = 3/h2
			paths.append(2)
		if d1 <= 4:
			h2 = h2+d1
			d1 = x*d1
			d1 = d1-4
			paths.append(3)
		else:
			h2 = 5*d1
			x = 6*x
			x = 5+9
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		h2 = d1**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))