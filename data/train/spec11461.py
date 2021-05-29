import numpy as np 

def function(x):

	w2 = 4
	b7 = x
	paths = []
	try:
		if w2 >= 3:
			b7 = 9+b7
			w2 = 7/w2
			w2 = w2*0
			paths.append(1)
		else:
			w2 = 9/w2
			x = 6+x
			w2 = 6*w2
			paths.append(2)
		if b7 < 7:
			w2 = 4*b7
			x = 2+x
			paths.append(3)
		else:
			x = 8*x
			w2 = 1-3
			x = b7-x
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