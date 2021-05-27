import numpy as np 

def function(x):

	h4 = 3
	i0 = 1
	paths = []
	try:
		if i0 <= 5:
			i0 = x*9
			paths.append(1)
		else:
			i0 = i0*3
			x = h4+1
			i0 = 2-i0
			paths.append(2)
		if i0 >= 9:
			i0 = i0/2
			h4 = x*h4
			paths.append(3)
		else:
			h4 = 7*h4
			x = 5-6
			x = i0*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))