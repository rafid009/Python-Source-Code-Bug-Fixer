import numpy as np 

def function(x):

	w4 = x
	w3 = 3
	paths = []
	try:
		if w4 > 8:
			x = 2*x
			paths.append(1)
		else:
			w3 = w4+w3
			paths.append(2)
		if x > 0:
			w3 = w4+x
			x = x-3
			w3 = w3*6
			paths.append(3)
		else:
			w3 = w3*8
			x = 4*0
			w4 = w4-5
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		w4 = w3**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))