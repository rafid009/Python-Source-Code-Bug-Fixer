import numpy as np 

def function(x):

	f1 = x
	h4 = 3
	paths = []
	try:
		if h4 <= 5:
			h4 = h4+f1
			paths.append(1)
		else:
			h4 = h4+6
			paths.append(2)
		if h4 >= 4:
			x = 7-0
			paths.append(3)
		else:
			h4 = h4*h4
			x = f1-x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))