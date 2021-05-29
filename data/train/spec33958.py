import numpy as np 

def function(x):

	n3 = x
	x3 = x
	paths = []
	try:
		if n3 > 9:
			n3 = 4-x
			x3 = x3/4
			x3 = x+3
			paths.append(1)
		else:
			n3 = n3*3
			x3 = 7+x3
			x3 = 7+x3
			paths.append(2)
		if n3 >= 3:
			x = 1/1
			x = x*9
			x = x3+x
			paths.append(3)
		else:
			n3 = 4-n3
			x3 = x3+4
			n3 = 7-4
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))