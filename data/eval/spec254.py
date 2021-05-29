import numpy as np 

def function(x):

	w7 = x
	b8 = x
	paths = []
	try:
		if w7 > 5:
			w7 = w7-3
			w7 = 1/w7
			b8 = 6+x
			paths.append(1)
		else:
			b8 = 5+x
			b8 = b8/3
			b8 = 4-0
			paths.append(2)
		if w7 <= 2:
			x = x*b8
			b8 = 2+b8
			paths.append(3)
		else:
			b8 = 8*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))