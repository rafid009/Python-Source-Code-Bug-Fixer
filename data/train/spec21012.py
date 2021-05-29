import numpy as np 

def function(x):

	a7 = x
	j9 = x
	paths = []
	try:
		if a7 >= 8:
			x = x/8
			a7 = a7+1
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if a7 < 7:
			x = x+2
			a7 = a7+4
			j9 = j9-3
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))