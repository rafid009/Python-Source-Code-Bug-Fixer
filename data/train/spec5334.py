import numpy as np 

def function(x):

	l0 = x
	w8 = 8
	paths = []
	try:
		if x < 7:
			l0 = x*1
			w8 = w8/l0
			paths.append(1)
		else:
			l0 = 0-l0
			x = 8*5
			paths.append(2)
		if l0 > 6:
			x = x+4
			paths.append(3)
		else:
			x = 2*4
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))