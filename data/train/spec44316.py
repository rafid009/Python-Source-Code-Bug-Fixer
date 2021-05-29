import numpy as np 

def function(x):

	m2 = 6
	w6 = x
	paths = []
	try:
		if w6 < 6:
			w6 = x*x
			paths.append(1)
		else:
			x = x-m2
			paths.append(2)
		if m2 >= 2:
			x = 9*x
			paths.append(3)
		else:
			w6 = 7+x
			m2 = 9/m2
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