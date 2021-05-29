import numpy as np 

def function(x):

	f8 = x
	h4 = x
	paths = []
	try:
		if h4 < 9:
			x = x-7
			paths.append(1)
		else:
			f8 = 2+f8
			paths.append(2)
		if f8 <= 6:
			h4 = 2/3
			paths.append(3)
		else:
			f8 = f8*7
			h4 = f8/h4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		h4 = f8**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))