import numpy as np 

def function(x):

	v9 = 7
	w9 = x
	paths = []
	try:
		if x > 8:
			w9 = 3-x
			paths.append(1)
		else:
			v9 = 0/4
			paths.append(2)
		if v9 > 7:
			w9 = 8+w9
			v9 = v9*2
			w9 = 8+w9
			paths.append(3)
		else:
			v9 = 1+x
			w9 = 7/6
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