import numpy as np 

def function(x):

	k2 = 0
	h5 = 2
	paths = []
	try:
		if x > 6:
			h5 = h5-k2
			paths.append(1)
		else:
			h5 = x*4
			k2 = x*k2
			h5 = k2-h5
			paths.append(2)
		if k2 <= 5:
			k2 = h5+h5
			k2 = k2-9
			h5 = 0+h5
			paths.append(3)
		else:
			k2 = k2*0
			h5 = k2/h5
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))