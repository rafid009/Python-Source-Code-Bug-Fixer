import numpy as np 

def function(x):

	h2 = x
	f4 = 2
	paths = []
	try:
		if f4 <= 4:
			x = x+7
			paths.append(1)
		else:
			f4 = x/1
			paths.append(2)
		if h2 < 9:
			f4 = f4-2
			paths.append(3)
		else:
			f4 = 7/x
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))