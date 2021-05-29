import numpy as np 

def function(x):

	w3 = 3
	w5 = 8
	paths = []
	try:
		if x < 6:
			w5 = x+5
			w3 = x*9
			w5 = w5/4
			paths.append(1)
		else:
			w5 = x/w5
			x = x-7
			paths.append(2)
		if w5 > 8:
			w3 = x-2
			w3 = w3*w3
			paths.append(3)
		else:
			w3 = w5/w3
			w3 = w3-3
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w3 = w5**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))