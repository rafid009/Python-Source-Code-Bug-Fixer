import numpy as np 

def function(x):

	v8 = 3
	x9 = x
	paths = []
	try:
		if x <= 7:
			v8 = 6-0
			x = x9/1
			paths.append(1)
		else:
			x9 = x9-2
			paths.append(2)
		if x > 6:
			x = 6-x
			paths.append(3)
		else:
			x = x+6
			x = x+5
			v8 = v8*x9
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