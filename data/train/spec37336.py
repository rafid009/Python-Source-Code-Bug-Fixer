import numpy as np 

def function(x):

	a5 = 8
	b7 = 8
	paths = []
	try:
		if x <= 8:
			a5 = a5+4
			a5 = a5+x
			paths.append(1)
		else:
			b7 = b7+2
			paths.append(2)
		if a5 <= 6:
			x = a5+x
			a5 = a5-3
			b7 = 7-b7
			paths.append(3)
		else:
			x = x/x
			a5 = b7-a5
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))