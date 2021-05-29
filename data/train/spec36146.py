import numpy as np 

def function(x):

	b9 = 8
	b4 = 2
	paths = []
	try:
		if x < 8:
			b9 = 2-5
			x = b4*b9
			x = x/8
			paths.append(1)
		else:
			b9 = b9*b4
			b4 = b4-3
			b9 = 2*b9
			paths.append(2)
		if b4 < 4:
			x = 4-x
			paths.append(3)
		else:
			x = 4-x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b9 = b4**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))