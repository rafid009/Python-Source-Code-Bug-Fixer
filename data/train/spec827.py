import numpy as np 

def function(x):

	f3 = 4
	h3 = x
	paths = []
	try:
		if h3 >= 3:
			f3 = f3-0
			paths.append(1)
		else:
			f3 = 9-f3
			x = x-x
			paths.append(2)
		if h3 < 9:
			f3 = 9/9
			f3 = 7/5
			f3 = f3*h3
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		h3 = f3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))