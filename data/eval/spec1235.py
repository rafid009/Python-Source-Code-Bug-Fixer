import numpy as np 

def function(x):

	h3 = 2
	j4 = 9
	paths = []
	try:
		if x < 4:
			h3 = h3+h3
			j4 = 0-x
			paths.append(1)
		else:
			h3 = 0*h3
			paths.append(2)
		if j4 <= 8:
			j4 = j4-0
			x = 3+x
			paths.append(3)
		else:
			j4 = 6-5
			h3 = 0+h3
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))