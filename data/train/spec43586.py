import numpy as np 

def function(x):

	i6 = x
	a6 = 2
	paths = []
	try:
		if i6 < 5:
			a6 = a6-8
			i6 = 5-x
			paths.append(1)
		else:
			x = x+6
			i6 = 0-x
			i6 = 6*9
			paths.append(2)
		if x < 7:
			a6 = a6*7
			x = 8*8
			paths.append(3)
		else:
			a6 = 1-4
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))