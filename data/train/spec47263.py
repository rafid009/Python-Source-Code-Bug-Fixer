import numpy as np 

def function(x):

	w9 = x
	b0 = 9
	paths = []
	try:
		if w9 < 1:
			b0 = 6/1
			paths.append(1)
		else:
			b0 = b0*b0
			b0 = b0-2
			paths.append(2)
		if x < 8:
			b0 = 6*b0
			w9 = 1/w9
			paths.append(3)
		else:
			w9 = w9-7
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		b0 = w9**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))