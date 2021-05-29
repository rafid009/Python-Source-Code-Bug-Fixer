import numpy as np 

def function(x):

	w7 = x
	b2 = 5
	paths = []
	try:
		if x < 0:
			x = x/2
			w7 = 3-w7
			b2 = b2*7
			paths.append(1)
		else:
			b2 = 1+x
			w7 = 1-w7
			paths.append(2)
		if b2 > 9:
			b2 = 6*b2
			x = x*9
			b2 = 5+b2
			paths.append(3)
		else:
			b2 = x/w7
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		w7 = b2**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))