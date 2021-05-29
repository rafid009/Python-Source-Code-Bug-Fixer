import numpy as np 

def function(x):

	w3 = 7
	f9 = x
	paths = []
	try:
		if f9 > 7:
			w3 = 2*2
			x = x/4
			paths.append(1)
		else:
			f9 = 0-f9
			w3 = 6*7
			x = x/x
			paths.append(2)
		if f9 <= 6:
			w3 = w3/f9
			w3 = 8-9
			f9 = 9-w3
			paths.append(3)
		else:
			f9 = 5+0
			x = 5+x
			x = x*f9
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))