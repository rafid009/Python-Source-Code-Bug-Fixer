import numpy as np 

def function(x):

	w8 = 5
	b0 = x
	paths = []
	try:
		if w8 > 2:
			x = x*b0
			x = x*x
			paths.append(1)
		else:
			b0 = b0/6
			w8 = 0/9
			x = w8+x
			paths.append(2)
		if x < 4:
			b0 = w8+4
			w8 = x*6
			b0 = 4+b0
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))