import numpy as np 

def function(x):

	b7 = x
	w4 = x
	paths = []
	try:
		if b7 < 2:
			x = 4+x
			w4 = w4-3
			w4 = w4*4
			paths.append(1)
		else:
			b7 = b7+4
			paths.append(2)
		if x > 4:
			w4 = w4*9
			x = x*x
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))