import numpy as np 

def function(x):

	h5 = 2
	f5 = x
	paths = []
	try:
		if x > 6:
			f5 = f5/9
			paths.append(1)
		else:
			x = x+f5
			h5 = x+8
			paths.append(2)
		if f5 >= 7:
			h5 = h5-x
			paths.append(3)
		else:
			f5 = x-9
			f5 = f5/1
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))