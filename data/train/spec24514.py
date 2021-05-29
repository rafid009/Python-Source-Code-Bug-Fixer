import numpy as np 

def function(x):

	w3 = x
	y3 = x
	paths = []
	try:
		if w3 > 4:
			w3 = w3+6
			paths.append(1)
		else:
			x = w3*6
			w3 = w3/x
			paths.append(2)
		if y3 <= 8:
			w3 = w3*0
			y3 = y3-1
			w3 = w3-9
			paths.append(3)
		else:
			y3 = 8*y3
			w3 = w3-w3
			y3 = 9+7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))