import numpy as np 

def function(x):

	b8 = 1
	a8 = x
	paths = []
	try:
		if a8 > 8:
			b8 = 3*b8
			x = x/1
			x = 9-x
			paths.append(1)
		else:
			x = x+x
			b8 = b8+2
			paths.append(2)
		if a8 <= 4:
			a8 = a8+3
			x = x-1
			paths.append(3)
		else:
			x = a8-5
			a8 = a8*b8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))