import numpy as np 

def function(x):

	j0 = 5
	i1 = x
	paths = []
	try:
		if i1 >= 6:
			j0 = j0/4
			paths.append(1)
		else:
			j0 = j0*i1
			paths.append(2)
		if j0 > 9:
			j0 = x-j0
			paths.append(3)
		else:
			j0 = j0-3
			i1 = 1-i1
			i1 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))