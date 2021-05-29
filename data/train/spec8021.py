import numpy as np 

def function(x):

	w0 = x
	l0 = x
	paths = []
	try:
		if l0 >= 9:
			l0 = 2/3
			l0 = l0+2
			paths.append(1)
		else:
			l0 = 8/l0
			w0 = w0/2
			paths.append(2)
		if l0 > 4:
			x = 5-0
			l0 = w0+1
			paths.append(3)
		else:
			l0 = l0-l0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w0 = w0**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))