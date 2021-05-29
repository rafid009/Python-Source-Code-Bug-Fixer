import numpy as np 

def function(x):

	v7 = 1
	b5 = x
	paths = []
	try:
		if b5 < 9:
			x = x-0
			v7 = b5+v7
			b5 = b5+v7
			paths.append(1)
		else:
			v7 = v7+6
			v7 = v7+3
			b5 = 5/v7
			paths.append(2)
		if x >= 3:
			v7 = b5/v7
			x = 0*x
			b5 = 3-b5
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))