import numpy as np 

def function(x):

	v9 = 5
	a8 = x
	paths = []
	try:
		if v9 < 2:
			v9 = 8+4
			a8 = a8+3
			paths.append(1)
		else:
			x = x-2
			x = a8*5
			a8 = v9-a8
			paths.append(2)
		if a8 > 6:
			x = x-x
			paths.append(3)
		else:
			v9 = v9-a8
			a8 = 1-a8
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		a8 = v9**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))