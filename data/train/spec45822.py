import numpy as np 

def function(x):

	b7 = x
	j9 = x
	paths = []
	try:
		if b7 > 8:
			x = 7-9
			x = b7-j9
			paths.append(1)
		else:
			j9 = 6/8
			paths.append(2)
		if b7 >= 6:
			x = b7-b7
			paths.append(3)
		else:
			x = 4*b7
			x = x*x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		j9 = b7**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))