import numpy as np 

def function(x):

	w1 = 7
	b8 = 1
	paths = []
	try:
		if b8 < 3:
			x = x+w1
			w1 = 2/w1
			paths.append(1)
		else:
			w1 = 3/w1
			w1 = w1*3
			w1 = x+w1
			paths.append(2)
		if x < 1:
			x = x*4
			w1 = w1+b8
			w1 = 3+w1
			paths.append(3)
		else:
			b8 = 2+b8
			w1 = x*4
			w1 = 5+b8
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