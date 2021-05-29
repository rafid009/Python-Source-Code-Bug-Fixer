import numpy as np 

def function(x):

	u2 = 6
	w3 = x
	paths = []
	try:
		if u2 <= 1:
			w3 = w3/9
			paths.append(1)
		else:
			w3 = w3*4
			paths.append(2)
		if u2 >= 8:
			w3 = w3*4
			x = x*7
			w3 = u2/u2
			paths.append(3)
		else:
			u2 = w3*5
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