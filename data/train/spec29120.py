import numpy as np 

def function(x):

	w1 = 4
	b5 = x
	paths = []
	try:
		if x > 4:
			x = x/b5
			w1 = 8-w1
			b5 = b5*3
			paths.append(1)
		else:
			w1 = 3/w1
			w1 = 2/w1
			paths.append(2)
		if w1 >= 8:
			x = x-0
			w1 = 8+x
			w1 = w1+1
			paths.append(3)
		else:
			w1 = x/6
			w1 = x/x
			b5 = 1*3
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