import numpy as np 

def function(x):

	i6 = x
	x3 = 7
	paths = []
	try:
		if i6 > 7:
			x = x-x3
			paths.append(1)
		else:
			x = i6+x
			paths.append(2)
		if x3 >= 7:
			x = i6*x
			x = 6+x
			x = x-x3
			paths.append(3)
		else:
			i6 = 7+x3
			i6 = i6/i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x3 = i6**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))