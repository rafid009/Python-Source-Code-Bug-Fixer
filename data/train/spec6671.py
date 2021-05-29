import numpy as np 

def function(x):

	h5 = x
	f8 = 1
	paths = []
	try:
		if f8 > 7:
			x = x*4
			f8 = f8*7
			x = h5/8
			paths.append(1)
		else:
			h5 = h5*4
			x = x+h5
			x = x/9
			paths.append(2)
		if x < 1:
			h5 = 5*h5
			f8 = 5*4
			h5 = h5-6
			paths.append(3)
		else:
			f8 = 0/f8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))