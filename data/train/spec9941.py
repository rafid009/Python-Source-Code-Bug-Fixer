import numpy as np 

def function(x):

	r8 = 4
	b4 = x
	paths = []
	try:
		if b4 < 1:
			x = r8-2
			r8 = r8+r8
			x = 0/x
			paths.append(1)
		else:
			b4 = b4-x
			paths.append(2)
		if r8 > 2:
			r8 = 7-5
			paths.append(3)
		else:
			r8 = 3/r8
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))