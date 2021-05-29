import numpy as np 

def function(x):

	w6 = x
	x = 3
	paths = []
	try:
		if w6 < 2:
			w6 = 3-w6
			w6 = w6-w6
			paths.append(1)
		else:
			x = x/7
			x = 3/x
			x = x/x
			paths.append(2)
		if w6 > 9:
			x = x/w6
			x = 9*w6
			paths.append(3)
		else:
			w6 = 0/1
			w6 = w6-1
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