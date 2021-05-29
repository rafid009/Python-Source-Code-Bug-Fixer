import numpy as np 

def function(x):

	h1 = 7
	f7 = x
	paths = []
	try:
		if f7 >= 8:
			f7 = 4/f7
			h1 = h1-9
			h1 = 2/f7
			paths.append(1)
		else:
			f7 = f7*8
			f7 = h1/h1
			h1 = h1+7
			paths.append(2)
		if h1 < 6:
			x = x+h1
			paths.append(3)
		else:
			f7 = h1/9
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))