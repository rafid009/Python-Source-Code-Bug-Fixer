import numpy as np 

def function(x):

	o1 = 9
	b7 = x
	paths = []
	try:
		if x < 3:
			b7 = 9/b7
			o1 = b7+o1
			paths.append(1)
		else:
			b7 = b7/3
			paths.append(2)
		if o1 <= 8:
			o1 = o1+6
			b7 = x*o1
			paths.append(3)
		else:
			x = 8/4
			b7 = b7/b7
			o1 = x-7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))