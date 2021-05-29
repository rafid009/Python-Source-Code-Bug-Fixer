import numpy as np 

def function(x):

	w0 = 6
	q7 = x
	x = 1
	paths = []
	try:
		if w0 < 6:
			q7 = 2+w0
			x = 7*7
			paths.append(1)
		else:
			q7 = 4-q7
			q7 = 8/q7
			paths.append(2)
		if x <= 8:
			x = 6+x
			paths.append(3)
		else:
			w0 = 1*w0
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		w0 = q7**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))