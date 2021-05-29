import numpy as np 

def function(x):

	b7 = 6
	w5 = 2
	paths = []
	try:
		if x >= 3:
			w5 = w5-9
			w5 = w5-4
			w5 = w5+8
			paths.append(1)
		else:
			w5 = x+2
			x = x-3
			paths.append(2)
		if w5 >= 0:
			x = b7/5
			b7 = w5-6
			paths.append(3)
		else:
			b7 = b7-0
			b7 = b7+1
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))