import numpy as np 

def function(x):

	w2 = x
	y7 = x
	paths = []
	try:
		if w2 < 6:
			x = 4*x
			paths.append(1)
		else:
			w2 = w2/7
			x = 1+x
			paths.append(2)
		if w2 >= 7:
			w2 = w2/9
			x = 7-y7
			paths.append(3)
		else:
			x = x/x
			y7 = w2+y7
			w2 = w2-4
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))