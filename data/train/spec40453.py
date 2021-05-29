import numpy as np 

def function(x):

	v3 = 5
	w2 = 5
	paths = []
	try:
		if x >= 0:
			w2 = w2+w2
			w2 = w2/v3
			paths.append(1)
		else:
			v3 = x*8
			paths.append(2)
		if v3 > 6:
			v3 = 3/v3
			w2 = 3*w2
			paths.append(3)
		else:
			v3 = 5-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))