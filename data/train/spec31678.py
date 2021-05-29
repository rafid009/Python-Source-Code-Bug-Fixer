import numpy as np 

def function(x):

	j7 = 3
	w9 = x
	paths = []
	try:
		if w9 >= 4:
			j7 = 6+j7
			paths.append(1)
		else:
			x = x-4
			w9 = w9+4
			j7 = 6-j7
			paths.append(2)
		if w9 >= 5:
			x = x-5
			x = 2+w9
			paths.append(3)
		else:
			x = 2/x
			j7 = j7-j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))