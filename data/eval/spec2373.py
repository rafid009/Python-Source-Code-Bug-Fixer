import numpy as np 

def function(x):

	a8 = 2
	w3 = x
	paths = []
	try:
		if w3 <= 3:
			x = a8/1
			x = a8*8
			paths.append(1)
		else:
			a8 = 0/8
			paths.append(2)
		if x <= 5:
			x = 0-x
			x = a8/x
			x = 7+5
			paths.append(3)
		else:
			a8 = a8-w3
			w3 = 7+w3
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))