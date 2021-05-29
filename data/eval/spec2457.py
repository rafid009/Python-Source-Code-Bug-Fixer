import numpy as np 

def function(x):

	n4 = 7
	i0 = 5
	paths = []
	try:
		if x > 9:
			n4 = i0+n4
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if i0 >= 7:
			i0 = 9+i0
			paths.append(3)
		else:
			i0 = 6-9
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))