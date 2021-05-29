import numpy as np 

def function(x):

	w0 = 9
	b3 = x
	paths = []
	try:
		if b3 < 1:
			x = x*x
			x = x+2
			b3 = 6-w0
			paths.append(1)
		else:
			w0 = 7*b3
			b3 = b3/5
			b3 = 3*8
			paths.append(2)
		if b3 <= 5:
			x = 3+w0
			paths.append(3)
		else:
			b3 = 6+w0
			b3 = b3+2
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))