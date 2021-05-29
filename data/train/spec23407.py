import numpy as np 

def function(x):

	x9 = x
	t8 = 0
	paths = []
	try:
		if x <= 8:
			x = 3-x
			paths.append(1)
		else:
			t8 = 5*6
			paths.append(2)
		if t8 >= 7:
			x9 = 7-x
			paths.append(3)
		else:
			x = x+t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))