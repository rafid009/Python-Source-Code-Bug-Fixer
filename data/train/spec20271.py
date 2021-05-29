import numpy as np 

def function(x):

	w3 = 7
	e0 = x
	paths = []
	try:
		if e0 >= 6:
			x = 9/x
			paths.append(1)
		else:
			w3 = x/4
			paths.append(2)
		if x >= 2:
			w3 = 1/7
			w3 = w3*0
			x = x-x
			paths.append(3)
		else:
			w3 = 7/w3
			w3 = e0+x
			e0 = w3+x
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