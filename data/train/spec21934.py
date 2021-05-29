import numpy as np 

def function(x):

	h2 = x
	k6 = x
	paths = []
	try:
		if x >= 4:
			h2 = 0+x
			paths.append(1)
		else:
			k6 = k6-6
			k6 = k6-k6
			k6 = k6-8
			paths.append(2)
		if h2 >= 6:
			x = x+2
			k6 = k6-5
			paths.append(3)
		else:
			k6 = x-3
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