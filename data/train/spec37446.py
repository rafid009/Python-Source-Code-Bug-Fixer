import numpy as np 

def function(x):

	v7 = 9
	j6 = x
	paths = []
	try:
		if x < 6:
			x = 5+x
			paths.append(1)
		else:
			v7 = 6*v7
			paths.append(2)
		if j6 < 2:
			x = j6-j6
			j6 = 1-4
			j6 = j6*2
			paths.append(3)
		else:
			x = x-v7
			j6 = 5*9
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