import numpy as np 

def function(x):

	h1 = x
	f9 = x
	paths = []
	try:
		if h1 >= 6:
			x = 1/4
			paths.append(1)
		else:
			f9 = 0*1
			paths.append(2)
		if x < 7:
			x = 2*9
			paths.append(3)
		else:
			x = f9+x
			f9 = f9+6
			h1 = 3*h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		f9 = h1**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))