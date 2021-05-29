import numpy as np 

def function(x):

	h4 = 9
	j4 = 4
	paths = []
	try:
		if h4 <= 9:
			j4 = j4-5
			h4 = h4+4
			paths.append(1)
		else:
			h4 = 0*h4
			h4 = 5/3
			paths.append(2)
		if x <= 6:
			h4 = 3-0
			h4 = h4*9
			h4 = 9+h4
			paths.append(3)
		else:
			h4 = x/6
			x = x-6
			x = x/9
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))