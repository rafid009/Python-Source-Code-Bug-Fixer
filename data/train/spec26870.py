import numpy as np 

def function(x):

	j0 = x
	k1 = x
	x = x
	paths = []
	try:
		if j0 > 5:
			j0 = 2-j0
			j0 = j0-6
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if k1 < 2:
			x = 9+x
			paths.append(3)
		else:
			k1 = 8-j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))