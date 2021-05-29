import numpy as np 

def function(x):

	n9 = 6
	i4 = 1
	x = 0
	paths = []
	try:
		if n9 >= 3:
			x = 2+2
			i4 = n9/3
			paths.append(1)
		else:
			n9 = n9*8
			n9 = n9+x
			paths.append(2)
		if x > 8:
			n9 = 0-1
			x = x+x
			i4 = 5+8
			paths.append(3)
		else:
			n9 = 3-n9
			x = 1-x
			x = n9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))