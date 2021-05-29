import numpy as np 

def function(x):

	h4 = 1
	i6 = 6
	paths = []
	try:
		if x <= 7:
			i6 = 3-i6
			paths.append(1)
		else:
			h4 = 8+h4
			h4 = h4-x
			i6 = i6+4
			paths.append(2)
		if h4 > 0:
			x = 0*x
			h4 = h4*h4
			paths.append(3)
		else:
			h4 = h4-i6
			x = i6+5
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))