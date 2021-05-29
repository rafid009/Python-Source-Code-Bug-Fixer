import numpy as np 

def function(x):

	b5 = 8
	w5 = 8
	paths = []
	try:
		if x >= 5:
			w5 = w5*8
			b5 = b5*9
			x = x+x
			paths.append(1)
		else:
			x = 0-1
			paths.append(2)
		if w5 < 9:
			b5 = b5-0
			b5 = b5+8
			paths.append(3)
		else:
			w5 = x*x
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))