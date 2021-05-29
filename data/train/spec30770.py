import numpy as np 

def function(x):

	f8 = 3
	w3 = x
	x = x
	paths = []
	try:
		if f8 < 1:
			x = 7/x
			paths.append(1)
		else:
			f8 = f8+x
			x = x/4
			f8 = f8-f8
			paths.append(2)
		if f8 <= 4:
			f8 = 7*x
			f8 = 4-f8
			x = x/w3
			paths.append(3)
		else:
			w3 = w3+8
			f8 = x-3
			x = x*3
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