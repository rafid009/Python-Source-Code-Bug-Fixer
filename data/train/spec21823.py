import numpy as np 

def function(x):

	v9 = 4
	j4 = x
	paths = []
	try:
		if j4 < 6:
			x = 8-x
			j4 = j4-v9
			v9 = j4*x
			paths.append(1)
		else:
			j4 = j4/x
			paths.append(2)
		if x >= 4:
			j4 = j4*x
			v9 = v9-3
			x = x/4
			paths.append(3)
		else:
			j4 = x-j4
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