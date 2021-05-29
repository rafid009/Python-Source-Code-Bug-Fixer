import numpy as np 

def function(x):

	y0 = 6
	w2 = 5
	paths = []
	try:
		if y0 <= 9:
			w2 = 2/w2
			x = x*y0
			y0 = y0-x
			paths.append(1)
		else:
			x = 0*w2
			paths.append(2)
		if x >= 5:
			w2 = x/4
			x = x/w2
			y0 = w2+y0
			paths.append(3)
		else:
			x = w2-5
			x = x*3
			w2 = w2*1
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		w2 = y0**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))