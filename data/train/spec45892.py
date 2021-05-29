import numpy as np 

def function(x):

	b7 = 4
	w2 = x
	paths = []
	try:
		if w2 <= 4:
			x = 5+x
			x = b7/w2
			paths.append(1)
		else:
			b7 = b7+7
			w2 = 7*w2
			x = x*x
			paths.append(2)
		if b7 >= 7:
			w2 = w2*x
			b7 = x-1
			paths.append(3)
		else:
			w2 = 4+7
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