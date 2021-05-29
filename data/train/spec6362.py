import numpy as np 

def function(x):

	h7 = 1
	j5 = 0
	paths = []
	try:
		if x > 5:
			h7 = h7-4
			x = x/5
			paths.append(1)
		else:
			h7 = 6/h7
			paths.append(2)
		if j5 >= 7:
			j5 = j5-h7
			paths.append(3)
		else:
			h7 = 4-h7
			j5 = h7-4
			h7 = h7/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))