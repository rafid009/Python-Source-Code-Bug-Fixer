import numpy as np 

def function(x):

	j4 = 5
	h4 = x
	x = 3
	paths = []
	try:
		if x <= 6:
			j4 = j4+j4
			j4 = j4*1
			paths.append(1)
		else:
			j4 = h4+j4
			h4 = h4-x
			x = x*x
			paths.append(2)
		if j4 >= 1:
			h4 = h4/1
			paths.append(3)
		else:
			j4 = 6/j4
			h4 = x*h4
			j4 = 5-x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		j4 = h4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))