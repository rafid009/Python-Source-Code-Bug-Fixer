import numpy as np 

def function(x):

	e8 = 5
	w2 = x
	paths = []
	try:
		if w2 > 5:
			w2 = 0/w2
			x = 9-0
			x = x/6
			paths.append(1)
		else:
			w2 = w2*9
			paths.append(2)
		if x <= 3:
			e8 = e8*3
			paths.append(3)
		else:
			w2 = e8/w2
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