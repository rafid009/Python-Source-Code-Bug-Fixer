import numpy as np 

def function(x):

	j3 = x
	z7 = x
	paths = []
	try:
		if j3 >= 0:
			j3 = j3-0
			j3 = j3/j3
			paths.append(1)
		else:
			j3 = 6-j3
			paths.append(2)
		if j3 >= 8:
			j3 = j3-j3
			paths.append(3)
		else:
			j3 = j3-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))