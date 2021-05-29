import numpy as np 

def function(x):

	h5 = x
	f8 = x
	paths = []
	try:
		if f8 <= 4:
			h5 = h5+f8
			paths.append(1)
		else:
			x = 1+x
			x = f8*x
			x = x*h5
			paths.append(2)
		if x > 6:
			f8 = 4*2
			paths.append(3)
		else:
			h5 = 6+6
			x = x*h5
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