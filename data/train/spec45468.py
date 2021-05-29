import numpy as np 

def function(x):

	i6 = x
	v7 = x
	paths = []
	try:
		if v7 < 8:
			v7 = v7*9
			paths.append(1)
		else:
			v7 = v7*1
			x = x-x
			v7 = v7/1
			paths.append(2)
		if x >= 7:
			i6 = i6*7
			paths.append(3)
		else:
			v7 = v7+8
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))