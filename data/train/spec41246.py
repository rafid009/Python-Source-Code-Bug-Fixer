import numpy as np 

def function(x):

	w0 = 7
	b4 = x
	paths = []
	try:
		if b4 <= 5:
			b4 = w0/b4
			paths.append(1)
		else:
			x = x*b4
			paths.append(2)
		if w0 > 5:
			x = 0+x
			w0 = 0/9
			x = x*1
			paths.append(3)
		else:
			w0 = x-w0
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))