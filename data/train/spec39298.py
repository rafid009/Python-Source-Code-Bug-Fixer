import numpy as np 

def function(x):

	x8 = x
	v5 = 1
	paths = []
	try:
		if x >= 7:
			x = 0-5
			paths.append(1)
		else:
			v5 = v5-x
			x8 = x8*3
			paths.append(2)
		if x >= 3:
			x8 = 7-v5
			paths.append(3)
		else:
			x = 5/9
			v5 = v5/5
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))