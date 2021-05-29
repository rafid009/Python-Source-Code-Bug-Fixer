import numpy as np 

def function(x):

	h5 = x
	f5 = x
	paths = []
	try:
		if h5 <= 8:
			h5 = x+h5
			paths.append(1)
		else:
			f5 = f5+9
			paths.append(2)
		if f5 >= 5:
			f5 = f5/2
			f5 = h5+f5
			paths.append(3)
		else:
			f5 = f5/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))