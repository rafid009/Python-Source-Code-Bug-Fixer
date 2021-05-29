import numpy as np 

def function(x):

	b3 = x
	w4 = 6
	paths = []
	try:
		if x >= 1:
			x = x+6
			x = 2/x
			w4 = w4/3
			paths.append(1)
		else:
			w4 = w4*4
			paths.append(2)
		if x <= 3:
			b3 = b3-1
			w4 = w4*x
			paths.append(3)
		else:
			w4 = 0+w4
			w4 = w4-x
			x = x*8
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))