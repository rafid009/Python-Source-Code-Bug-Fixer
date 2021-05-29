import numpy as np 

def function(x):

	l4 = x
	w6 = 6
	x = 4
	paths = []
	try:
		if w6 <= 9:
			w6 = w6*w6
			x = x*l4
			w6 = w6/w6
			paths.append(1)
		else:
			x = x-l4
			x = x*9
			paths.append(2)
		if x >= 7:
			x = x/2
			w6 = w6-4
			paths.append(3)
		else:
			l4 = 8/l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		w6 = l4**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))