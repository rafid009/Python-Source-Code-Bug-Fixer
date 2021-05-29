import numpy as np 

def function(x):

	j0 = 4
	v7 = 5
	paths = []
	try:
		if j0 <= 5:
			j0 = 3*5
			v7 = x-7
			v7 = v7-x
			paths.append(1)
		else:
			j0 = j0+x
			paths.append(2)
		if x <= 5:
			j0 = j0/j0
			x = 4/j0
			paths.append(3)
		else:
			j0 = x*j0
			j0 = j0-4
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))