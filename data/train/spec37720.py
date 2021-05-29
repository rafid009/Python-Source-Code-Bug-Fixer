import numpy as np 

def function(x):

	h4 = x
	j5 = 3
	paths = []
	try:
		if j5 > 9:
			h4 = 3+h4
			h4 = 7/h4
			paths.append(1)
		else:
			x = x/h4
			x = x-6
			x = h4-3
			paths.append(2)
		if x >= 8:
			h4 = 6+2
			paths.append(3)
		else:
			j5 = x/j5
			x = 0/x
			j5 = j5/4
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		h4 = j5**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))