import numpy as np 

def function(x):

	i5 = 9
	h2 = x
	paths = []
	try:
		if h2 < 8:
			i5 = 6-8
			paths.append(1)
		else:
			h2 = 0+h2
			h2 = 4/h2
			paths.append(2)
		if x < 6:
			h2 = h2-8
			paths.append(3)
		else:
			i5 = i5*h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))