import numpy as np 

def function(x):

	h3 = 7
	k8 = 3
	paths = []
	try:
		if x >= 8:
			x = 4+2
			paths.append(1)
		else:
			x = x+5
			h3 = 0-h3
			paths.append(2)
		if k8 <= 0:
			x = 2-4
			h3 = 1/h3
			paths.append(3)
		else:
			h3 = h3+7
			h3 = 4-h3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))