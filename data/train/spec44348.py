import numpy as np 

def function(x):

	a6 = 8
	b6 = x
	x = 3
	paths = []
	try:
		if b6 >= 6:
			a6 = a6+b6
			x = x+a6
			paths.append(1)
		else:
			a6 = 0+6
			paths.append(2)
		if a6 >= 8:
			a6 = x/1
			b6 = 3-b6
			x = x/1
			paths.append(3)
		else:
			x = 1-b6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))