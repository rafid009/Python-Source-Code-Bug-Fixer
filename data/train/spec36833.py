import numpy as np 

def function(x):

	y5 = 0
	w8 = 2
	paths = []
	try:
		if x < 4:
			x = x+8
			y5 = w8*y5
			paths.append(1)
		else:
			w8 = y5/w8
			paths.append(2)
		if y5 > 6:
			y5 = y5/8
			y5 = y5*2
			paths.append(3)
		else:
			w8 = 3*x
			y5 = 7+x
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))