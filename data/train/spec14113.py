import numpy as np 

def function(x):

	q6 = 5
	w4 = x
	paths = []
	try:
		if w4 > 9:
			x = 5*0
			paths.append(1)
		else:
			x = 9*x
			x = w4+x
			q6 = 9+q6
			paths.append(2)
		if w4 > 0:
			q6 = 6-1
			paths.append(3)
		else:
			q6 = 4+1
			w4 = w4/2
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