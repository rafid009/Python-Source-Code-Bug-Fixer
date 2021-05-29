import numpy as np 

def function(x):

	j6 = x
	h7 = x
	paths = []
	try:
		if x > 8:
			j6 = j6/h7
			j6 = j6/7
			h7 = 8*h7
			paths.append(1)
		else:
			j6 = 1+j6
			j6 = j6-9
			paths.append(2)
		if h7 > 3:
			h7 = h7-h7
			j6 = 3+j6
			h7 = h7-8
			paths.append(3)
		else:
			h7 = 2-h7
			j6 = h7*j6
			j6 = j6/j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		h7 = j6**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))