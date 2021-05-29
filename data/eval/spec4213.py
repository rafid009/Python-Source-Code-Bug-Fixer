import numpy as np 

def function(x):

	w4 = 4
	f1 = 6
	paths = []
	try:
		if x > 8:
			x = x/x
			w4 = x/w4
			f1 = f1+3
			paths.append(1)
		else:
			w4 = x+6
			x = x+0
			paths.append(2)
		if x > 6:
			x = 6/x
			x = x-w4
			x = x*2
			paths.append(3)
		else:
			w4 = w4+x
			f1 = f1+7
			f1 = f1+2
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))