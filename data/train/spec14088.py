import numpy as np 

def function(x):

	v7 = 4
	j9 = 3
	paths = []
	try:
		if v7 < 9:
			v7 = v7/9
			j9 = j9-6
			paths.append(1)
		else:
			v7 = 6*v7
			x = v7+3
			paths.append(2)
		if v7 >= 0:
			j9 = j9*6
			paths.append(3)
		else:
			x = 5/x
			j9 = j9+9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))