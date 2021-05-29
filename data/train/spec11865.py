import numpy as np 

def function(x):

	w2 = 4
	e1 = 7
	paths = []
	try:
		if e1 < 1:
			w2 = 1*7
			w2 = 2*9
			w2 = x+5
			paths.append(1)
		else:
			e1 = e1+4
			x = 0-8
			x = x+3
			paths.append(2)
		if e1 > 4:
			e1 = 9/e1
			w2 = w2/7
			paths.append(3)
		else:
			w2 = 2+1
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