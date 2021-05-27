import numpy as np 

def function(x):

	h2 = x
	d6 = 5
	paths = []
	try:
		if h2 < 3:
			h2 = h2/5
			paths.append(1)
		else:
			d6 = 7*d6
			d6 = d6+1
			paths.append(2)
		if d6 > 2:
			h2 = h2-6
			paths.append(3)
		else:
			d6 = h2*6
			x = x-5
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