import numpy as np 

def function(x):

	i5 = x
	x9 = 8
	paths = []
	try:
		if i5 >= 3:
			i5 = 1/2
			x9 = x9-3
			i5 = i5+0
			paths.append(1)
		else:
			x9 = x*4
			x9 = x9+6
			x = 4+5
			paths.append(2)
		if i5 < 6:
			i5 = i5-3
			paths.append(3)
		else:
			i5 = 2/9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))