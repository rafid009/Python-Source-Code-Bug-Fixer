import numpy as np 

def function(x):

	w6 = 7
	i9 = x
	paths = []
	try:
		if x < 1:
			w6 = x-7
			x = x+x
			paths.append(1)
		else:
			i9 = 0-i9
			paths.append(2)
		if x >= 8:
			x = x+3
			i9 = x*9
			paths.append(3)
		else:
			i9 = x+3
			i9 = i9-3
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))