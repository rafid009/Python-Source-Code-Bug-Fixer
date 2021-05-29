import numpy as np 

def function(x):

	b7 = 3
	o6 = 4
	paths = []
	try:
		if b7 >= 9:
			b7 = 2-b7
			b7 = 5-b7
			b7 = 8/o6
			paths.append(1)
		else:
			b7 = b7-9
			x = 0/b7
			o6 = o6+o6
			paths.append(2)
		if x < 3:
			x = o6+x
			paths.append(3)
		else:
			b7 = o6*b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))