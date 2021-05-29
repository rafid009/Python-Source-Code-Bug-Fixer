import numpy as np 

def function(x):

	i4 = 3
	n8 = 9
	paths = []
	try:
		if i4 > 1:
			x = 1-x
			paths.append(1)
		else:
			x = 9-6
			i4 = 6*7
			x = x*0
			paths.append(2)
		if x >= 2:
			i4 = i4*4
			n8 = n8/n8
			paths.append(3)
		else:
			n8 = 9/8
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