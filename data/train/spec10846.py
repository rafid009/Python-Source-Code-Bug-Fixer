import numpy as np 

def function(x):

	w0 = 7
	q1 = 3
	paths = []
	try:
		if w0 <= 6:
			q1 = q1+7
			paths.append(1)
		else:
			q1 = x*7
			x = x*1
			x = 4+x
			paths.append(2)
		if x < 6:
			x = 6/x
			paths.append(3)
		else:
			w0 = w0*5
			w0 = 1*8
			w0 = w0-w0
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		w0 = q1**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))