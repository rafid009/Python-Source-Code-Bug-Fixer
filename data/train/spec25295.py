import numpy as np 

def function(x):

	i9 = 9
	n2 = x
	paths = []
	try:
		if n2 > 6:
			n2 = i9/5
			n2 = n2*7
			n2 = i9+n2
			paths.append(1)
		else:
			n2 = n2+0
			x = x/x
			paths.append(2)
		if i9 < 0:
			i9 = 0-3
			paths.append(3)
		else:
			n2 = n2+6
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))