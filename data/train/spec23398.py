import numpy as np 

def function(x):

	n7 = x
	f8 = x
	paths = []
	try:
		if n7 >= 9:
			n7 = n7+n7
			paths.append(1)
		else:
			f8 = 6*7
			f8 = 4-f8
			paths.append(2)
		if x < 2:
			f8 = 2-f8
			f8 = 0*f8
			n7 = n7+3
			paths.append(3)
		else:
			f8 = f8*0
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