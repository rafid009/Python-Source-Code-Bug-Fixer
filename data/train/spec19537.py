import numpy as np 

def function(x):

	j2 = x
	x2 = 7
	paths = []
	try:
		if x2 >= 6:
			x2 = j2-1
			paths.append(1)
		else:
			j2 = x-j2
			j2 = j2*j2
			paths.append(2)
		if x2 <= 5:
			j2 = j2*6
			paths.append(3)
		else:
			x2 = x2-x
			x2 = 2/3
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