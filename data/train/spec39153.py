import numpy as np 

def function(x):

	n3 = x
	i4 = 8
	paths = []
	try:
		if x < 4:
			x = n3+x
			i4 = 9/4
			paths.append(1)
		else:
			n3 = i4/n3
			n3 = 4/n3
			i4 = i4-8
			paths.append(2)
		if n3 > 8:
			i4 = 3-i4
			n3 = n3+4
			i4 = 9*9
			paths.append(3)
		else:
			i4 = i4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))