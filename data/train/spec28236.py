import numpy as np 

def function(x):

	y7 = 1
	w3 = 9
	paths = []
	try:
		if w3 < 1:
			x = x*x
			x = x*0
			paths.append(1)
		else:
			w3 = x-w3
			paths.append(2)
		if x >= 4:
			y7 = 1*y7
			paths.append(3)
		else:
			x = y7-0
			w3 = 9-w3
			x = x*w3
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