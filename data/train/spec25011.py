import numpy as np 

def function(x):

	b9 = 8
	q4 = x
	paths = []
	try:
		if q4 < 7:
			x = x/x
			paths.append(1)
		else:
			x = 0+b9
			q4 = b9-q4
			paths.append(2)
		if b9 >= 6:
			b9 = b9/b9
			paths.append(3)
		else:
			b9 = b9*9
			b9 = b9+0
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		b9 = q4**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))