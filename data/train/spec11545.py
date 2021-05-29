import numpy as np 

def function(x):

	f9 = x
	h2 = x
	paths = []
	try:
		if h2 >= 5:
			x = x*6
			h2 = 1-8
			f9 = f9+x
			paths.append(1)
		else:
			f9 = f9+4
			f9 = f9*4
			paths.append(2)
		if f9 < 8:
			h2 = f9-7
			paths.append(3)
		else:
			x = x+x
			f9 = 9-f9
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		f9 = h2**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))