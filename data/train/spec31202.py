import numpy as np 

def function(x):

	n1 = x
	i9 = 1
	paths = []
	try:
		if i9 < 9:
			n1 = 9*8
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if i9 > 6:
			x = x/n1
			x = x+x
			paths.append(3)
		else:
			n1 = n1+2
			n1 = i9/n1
			i9 = i9*n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))