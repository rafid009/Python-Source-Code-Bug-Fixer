import numpy as np 

def function(x):

	n1 = x
	i9 = x
	paths = []
	try:
		if x > 3:
			x = 0+n1
			paths.append(1)
		else:
			i9 = i9/n1
			paths.append(2)
		if x <= 4:
			i9 = i9+i9
			i9 = i9*i9
			i9 = i9*n1
			paths.append(3)
		else:
			x = x+8
			x = x*4
			x = i9-x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))