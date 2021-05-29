import numpy as np 

def function(x):

	e8 = 1
	j6 = 8
	paths = []
	try:
		if e8 >= 1:
			j6 = j6*3
			j6 = j6*3
			x = 1+x
			paths.append(1)
		else:
			j6 = j6-e8
			e8 = j6*e8
			x = 4-0
			paths.append(2)
		if x >= 8:
			e8 = j6-8
			e8 = 1-5
			j6 = 0-j6
			paths.append(3)
		else:
			j6 = 3*j6
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