import numpy as np 

def function(x):

	j6 = 2
	e9 = x
	paths = []
	try:
		if j6 <= 6:
			e9 = e9*2
			paths.append(1)
		else:
			j6 = j6*j6
			paths.append(2)
		if e9 >= 9:
			j6 = 9-7
			paths.append(3)
		else:
			e9 = e9-2
			e9 = 0+x
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