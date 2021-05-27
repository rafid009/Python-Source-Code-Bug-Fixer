import numpy as np 

def function(x):

	h0 = 9
	j5 = 7
	paths = []
	try:
		if h0 > 5:
			h0 = h0-h0
			paths.append(1)
		else:
			j5 = j5/j5
			j5 = j5-8
			paths.append(2)
		if x > 9:
			j5 = x/j5
			j5 = j5-x
			x = 1/x
			paths.append(3)
		else:
			j5 = 5-j5
			h0 = h0+5
			x = x/x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))