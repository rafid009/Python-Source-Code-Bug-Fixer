import numpy as np 

def function(x):

	h5 = 1
	f4 = x
	paths = []
	try:
		if x > 3:
			f4 = f4/6
			h5 = h5*x
			h5 = 4-f4
			paths.append(1)
		else:
			f4 = x+x
			paths.append(2)
		if h5 >= 8:
			f4 = f4*2
			paths.append(3)
		else:
			h5 = 3-x
			h5 = 6*h5
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))