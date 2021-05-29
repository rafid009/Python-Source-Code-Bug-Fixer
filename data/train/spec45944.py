import numpy as np 

def function(x):

	e3 = 3
	w6 = x
	paths = []
	try:
		if e3 >= 7:
			w6 = 6-w6
			w6 = e3/4
			w6 = w6+w6
			paths.append(1)
		else:
			w6 = x+7
			paths.append(2)
		if w6 > 0:
			w6 = w6/w6
			e3 = 5+e3
			x = 9*x
			paths.append(3)
		else:
			x = 0/w6
			x = x+3
			e3 = 6/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))