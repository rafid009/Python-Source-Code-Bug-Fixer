import numpy as np 

def function(x):

	x4 = 2
	w8 = x
	paths = []
	try:
		if x4 > 9:
			x4 = 7/x
			w8 = 2+4
			x4 = 6+x4
			paths.append(1)
		else:
			w8 = x4/7
			w8 = 1/5
			x = x/3
			paths.append(2)
		if x4 <= 1:
			x4 = x4+4
			x = x4/x4
			w8 = w8*2
			paths.append(3)
		else:
			x4 = 6/x4
			x = 1+x
			w8 = x*w8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))