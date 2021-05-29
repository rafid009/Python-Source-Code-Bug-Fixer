import numpy as np 

def function(x):

	x6 = x
	w6 = 5
	paths = []
	try:
		if w6 <= 7:
			w6 = 9+w6
			paths.append(1)
		else:
			x = 1-x6
			paths.append(2)
		if x >= 4:
			w6 = w6+2
			paths.append(3)
		else:
			x6 = x/5
			w6 = 1+w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))