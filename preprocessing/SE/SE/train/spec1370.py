import numpy as np 

def function(x):

	j4 = x
	g9 = 0
	paths = []
	try:
		if x < 6:
			x = 4-9
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if j4 < 6:
			x = 8+x
			paths.append(3)
		else:
			x = x-j4
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