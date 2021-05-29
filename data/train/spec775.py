import numpy as np 

def function(x):

	i6 = x
	j4 = x
	paths = []
	try:
		if i6 < 5:
			x = 5/x
			paths.append(1)
		else:
			j4 = j4-8
			j4 = i6-x
			paths.append(2)
		if j4 < 7:
			i6 = j4+i6
			i6 = 0*j4
			paths.append(3)
		else:
			j4 = 7/j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))