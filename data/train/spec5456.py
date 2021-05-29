import numpy as np 

def function(x):

	f2 = x
	h6 = x
	paths = []
	try:
		if f2 <= 8:
			h6 = h6*f2
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if f2 < 9:
			f2 = f2/6
			paths.append(3)
		else:
			f2 = f2/3
			f2 = f2*9
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		h6 = f2**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))