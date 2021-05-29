import numpy as np 

def function(x):

	e8 = x
	i9 = x
	paths = []
	try:
		if e8 <= 1:
			i9 = 4/e8
			paths.append(1)
		else:
			i9 = 9/i9
			paths.append(2)
		if i9 > 2:
			i9 = i9+4
			e8 = e8-1
			paths.append(3)
		else:
			i9 = i9+5
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))