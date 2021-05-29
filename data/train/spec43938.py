import numpy as np 

def function(x):

	e6 = 6
	w3 = x
	paths = []
	try:
		if x > 6:
			w3 = 7+5
			x = 5+x
			x = x-5
			paths.append(1)
		else:
			e6 = e6+0
			paths.append(2)
		if e6 < 8:
			e6 = 4/e6
			e6 = e6*e6
			e6 = e6+e6
			paths.append(3)
		else:
			e6 = 2*x
			e6 = 4-9
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		w3 = w3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))