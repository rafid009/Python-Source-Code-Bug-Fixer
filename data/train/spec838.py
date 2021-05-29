import numpy as np 

def function(x):

	h7 = 4
	x1 = x
	x = 1
	paths = []
	try:
		if x1 <= 4:
			h7 = x1/3
			x = x*h7
			x = 3/7
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if x1 >= 2:
			x1 = 0/h7
			paths.append(3)
		else:
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		h7 = x1**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))