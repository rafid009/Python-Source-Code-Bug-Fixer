import numpy as np 

def function(x):

	q3 = 2
	w6 = x
	paths = []
	try:
		if w6 >= 2:
			x = 0*x
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if w6 < 0:
			x = 8*w6
			q3 = q3+6
			x = w6+w6
			paths.append(3)
		else:
			x = x+5
			x = 8/x
			w6 = w6-6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))