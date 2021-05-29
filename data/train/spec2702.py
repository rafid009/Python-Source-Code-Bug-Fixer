import numpy as np 

def function(x):

	f0 = 5
	h5 = 1
	paths = []
	try:
		if f0 >= 4:
			f0 = 6*x
			h5 = h5/5
			f0 = 2-6
			paths.append(1)
		else:
			x = x/f0
			f0 = f0/8
			x = x+7
			paths.append(2)
		if x >= 7:
			x = x-h5
			paths.append(3)
		else:
			h5 = x*1
			f0 = h5+x
			f0 = 8*f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		h5 = f0**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))