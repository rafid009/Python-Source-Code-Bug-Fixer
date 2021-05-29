import numpy as np 

def function(x):

	h4 = 9
	j6 = 6
	paths = []
	try:
		if x < 0:
			j6 = j6-3
			j6 = j6-4
			paths.append(1)
		else:
			h4 = h4+j6
			paths.append(2)
		if j6 >= 5:
			j6 = j6/8
			paths.append(3)
		else:
			h4 = h4+4
			h4 = h4/h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))