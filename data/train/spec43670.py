import numpy as np 

def function(x):

	i4 = 9
	k5 = 9
	paths = []
	try:
		if k5 >= 7:
			k5 = 3+k5
			x = 6/x
			paths.append(1)
		else:
			x = 4+x
			i4 = 7+0
			x = 1-x
			paths.append(2)
		if k5 <= 5:
			i4 = k5+5
			paths.append(3)
		else:
			k5 = 8+k5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))