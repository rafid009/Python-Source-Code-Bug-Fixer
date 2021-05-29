import numpy as np 

def function(x):

	j8 = x
	w2 = x
	paths = []
	try:
		if j8 < 1:
			w2 = j8+3
			x = x-j8
			x = w2*w2
			paths.append(1)
		else:
			w2 = j8+w2
			j8 = 0*6
			w2 = 4-w2
			paths.append(2)
		if w2 <= 7:
			x = x-5
			w2 = 0/w2
			paths.append(3)
		else:
			w2 = w2*4
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