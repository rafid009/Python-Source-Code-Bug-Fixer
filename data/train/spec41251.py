import numpy as np 

def function(x):

	g5 = 5
	w8 = x
	paths = []
	try:
		if x <= 8:
			g5 = g5-0
			w8 = w8+8
			x = x+3
			paths.append(1)
		else:
			w8 = w8*9
			paths.append(2)
		if w8 > 0:
			w8 = w8+x
			g5 = 5+4
			x = w8*x
			paths.append(3)
		else:
			w8 = w8*6
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))