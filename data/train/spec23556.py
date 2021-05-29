import numpy as np 

def function(x):

	v3 = x
	j9 = 1
	x = x
	paths = []
	try:
		if x > 7:
			j9 = j9+7
			paths.append(1)
		else:
			j9 = x-6
			paths.append(2)
		if j9 < 1:
			j9 = j9-0
			j9 = j9*v3
			paths.append(3)
		else:
			j9 = x*j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))