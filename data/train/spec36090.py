import numpy as np 

def function(x):

	h0 = 6
	k6 = 1
	paths = []
	try:
		if x >= 0:
			k6 = 2+k6
			paths.append(1)
		else:
			x = k6-6
			k6 = x-k6
			paths.append(2)
		if k6 < 0:
			x = 8+3
			h0 = 6*h0
			paths.append(3)
		else:
			k6 = 0/k6
			x = 1/x
			k6 = k6-0
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))