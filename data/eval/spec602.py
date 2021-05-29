import numpy as np 

def function(x):

	x8 = x
	v9 = 7
	paths = []
	try:
		if x < 5:
			v9 = v9*3
			paths.append(1)
		else:
			v9 = 6+x
			v9 = 8+v9
			x8 = x-x8
			paths.append(2)
		if x8 > 6:
			v9 = x+v9
			paths.append(3)
		else:
			x8 = x+v9
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		v9 = x8**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))