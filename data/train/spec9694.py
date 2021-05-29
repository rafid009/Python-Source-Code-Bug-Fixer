import numpy as np 

def function(x):

	b4 = 2
	a2 = 6
	paths = []
	try:
		if x >= 2:
			a2 = 4/2
			x = a2/3
			b4 = 2+2
			paths.append(1)
		else:
			b4 = 4-b4
			x = x-1
			paths.append(2)
		if x >= 3:
			b4 = x+6
			x = 8+x
			paths.append(3)
		else:
			b4 = b4+x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		a2 = b4**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))