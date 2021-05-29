import numpy as np 

def function(x):

	v7 = 6
	i1 = x
	paths = []
	try:
		if i1 < 4:
			v7 = v7-0
			v7 = 4/9
			paths.append(1)
		else:
			i1 = i1*3
			v7 = v7*5
			x = 9-1
			paths.append(2)
		if i1 < 4:
			i1 = 5+i1
			v7 = 8+v7
			paths.append(3)
		else:
			v7 = v7/v7
			v7 = 1/v7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))