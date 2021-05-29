import numpy as np 

def function(x):

	l1 = x
	w0 = x
	paths = []
	try:
		if w0 > 6:
			w0 = w0+7
			l1 = 2*w0
			paths.append(1)
		else:
			l1 = x/l1
			x = 7*x
			paths.append(2)
		if l1 <= 4:
			x = x-5
			l1 = 0-l1
			paths.append(3)
		else:
			l1 = l1/6
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