import numpy as np 

def function(x):

	d4 = 5
	b8 = 1
	paths = []
	try:
		if x > 6:
			b8 = b8-1
			paths.append(1)
		else:
			b8 = 1*b8
			paths.append(2)
		if x < 2:
			b8 = b8/x
			b8 = x+6
			paths.append(3)
		else:
			d4 = d4+d4
			d4 = b8-8
			x = 6/d4
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))