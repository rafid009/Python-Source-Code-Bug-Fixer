import numpy as np 

def function(x):

	o4 = 8
	w2 = 4
	paths = []
	try:
		if x >= 9:
			w2 = 2+w2
			w2 = w2-9
			paths.append(1)
		else:
			x = 4*x
			o4 = 6*o4
			paths.append(2)
		if x < 4:
			x = w2+x
			paths.append(3)
		else:
			w2 = 8+w2
			o4 = o4-9
			o4 = 0/7
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