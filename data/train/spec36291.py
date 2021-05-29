import numpy as np 

def function(x):

	n2 = 3
	i8 = x
	paths = []
	try:
		if n2 < 2:
			i8 = i8/x
			n2 = 4+i8
			paths.append(1)
		else:
			n2 = 8+2
			paths.append(2)
		if i8 <= 7:
			i8 = 0/9
			paths.append(3)
		else:
			x = x+8
			x = 9-7
			i8 = i8-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))