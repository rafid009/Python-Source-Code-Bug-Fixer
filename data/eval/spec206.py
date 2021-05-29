import numpy as np 

def function(x):

	w8 = x
	y4 = 9
	paths = []
	try:
		if x < 5:
			w8 = w8+5
			paths.append(1)
		else:
			x = y4-0
			w8 = w8-x
			paths.append(2)
		if y4 > 9:
			y4 = y4*8
			paths.append(3)
		else:
			w8 = w8/3
			x = x*6
			y4 = 4+x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		w8 = y4**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))