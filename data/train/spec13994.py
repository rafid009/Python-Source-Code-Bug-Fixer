import numpy as np 

def function(x):

	a9 = x
	j3 = x
	paths = []
	try:
		if x <= 2:
			a9 = a9-a9
			x = x-5
			paths.append(1)
		else:
			j3 = 3+j3
			paths.append(2)
		if j3 >= 2:
			x = x-3
			paths.append(3)
		else:
			j3 = j3+j3
			a9 = 8/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))