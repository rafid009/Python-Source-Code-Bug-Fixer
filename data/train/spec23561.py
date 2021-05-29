import numpy as np 

def function(x):

	f9 = x
	h4 = x
	paths = []
	try:
		if h4 <= 5:
			x = 6-x
			h4 = 5-5
			paths.append(1)
		else:
			f9 = f9+h4
			paths.append(2)
		if x >= 8:
			f9 = f9*9
			f9 = f9+f9
			paths.append(3)
		else:
			f9 = 8-f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		h4 = f9**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))