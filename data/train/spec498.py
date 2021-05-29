import numpy as np 

def function(x):

	a2 = x
	w8 = 5
	paths = []
	try:
		if x <= 1:
			w8 = 9*w8
			w8 = x+4
			paths.append(1)
		else:
			x = a2+3
			w8 = w8+5
			paths.append(2)
		if w8 <= 8:
			w8 = w8+5
			paths.append(3)
		else:
			x = x+a2
			a2 = 8*5
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		a2 = w8**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))