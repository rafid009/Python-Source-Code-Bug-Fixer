import numpy as np 

def function(x):

	f7 = 9
	w6 = x
	paths = []
	try:
		if w6 <= 9:
			w6 = w6-x
			f7 = f7+4
			paths.append(1)
		else:
			x = 9-x
			w6 = w6*5
			f7 = f7-f7
			paths.append(2)
		if x > 2:
			w6 = w6*f7
			paths.append(3)
		else:
			f7 = f7*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))