import numpy as np 

def function(x):

	w2 = 7
	f1 = 8
	paths = []
	try:
		if w2 < 8:
			x = 2-x
			x = 0+x
			paths.append(1)
		else:
			f1 = f1+f1
			w2 = 3+w2
			w2 = w2+2
			paths.append(2)
		if w2 < 0:
			f1 = f1-1
			x = 4+x
			x = x+w2
			paths.append(3)
		else:
			f1 = 0*x
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