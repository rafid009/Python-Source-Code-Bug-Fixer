import numpy as np 

def function(x):

	b8 = 9
	w1 = 2
	paths = []
	try:
		if w1 > 9:
			b8 = b8-w1
			w1 = 2+5
			paths.append(1)
		else:
			x = 7/x
			w1 = w1+0
			b8 = b8*b8
			paths.append(2)
		if x < 4:
			w1 = w1/9
			paths.append(3)
		else:
			x = b8*x
			w1 = w1*9
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