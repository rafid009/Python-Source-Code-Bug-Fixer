import numpy as np 

def function(x):

	w3 = 3
	x7 = x
	x = 2
	paths = []
	try:
		if x > 3:
			w3 = x/5
			x7 = x7/1
			x7 = x7-1
			paths.append(1)
		else:
			x = x*9
			w3 = w3*4
			x = 6-x7
			paths.append(2)
		if x7 <= 6:
			x = x7/x
			x = 3-7
			paths.append(3)
		else:
			w3 = 4/8
			w3 = w3*x
			w3 = w3-x7
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x7 = w3**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))