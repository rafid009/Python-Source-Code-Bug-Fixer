import numpy as np 

def function(x):

	i1 = x
	j3 = 1
	paths = []
	try:
		if j3 > 7:
			i1 = x-1
			paths.append(1)
		else:
			j3 = 2/j3
			x = 2-4
			paths.append(2)
		if i1 < 3:
			j3 = i1/2
			x = x-8
			x = 2+j3
			paths.append(3)
		else:
			i1 = i1+7
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