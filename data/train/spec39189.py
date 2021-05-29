import numpy as np 

def function(x):

	v8 = x
	x9 = x
	paths = []
	try:
		if x9 >= 9:
			x = 5-x
			x = x*6
			paths.append(1)
		else:
			v8 = 4*v8
			paths.append(2)
		if x9 >= 3:
			x9 = x9*3
			paths.append(3)
		else:
			v8 = v8-9
			v8 = v8*6
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))