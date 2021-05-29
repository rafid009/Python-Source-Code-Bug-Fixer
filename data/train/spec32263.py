import numpy as np 

def function(x):

	i7 = x
	n0 = x
	x = 7
	paths = []
	try:
		if n0 < 1:
			x = x+4
			n0 = n0+n0
			paths.append(1)
		else:
			x = n0+x
			n0 = n0+1
			x = x-n0
			paths.append(2)
		if x >= 1:
			i7 = i7/9
			x = x+x
			x = 5/8
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		i7 = n0**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))