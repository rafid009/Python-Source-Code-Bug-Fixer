import numpy as np 

def function(x):

	l9 = x
	w1 = x
	paths = []
	try:
		if w1 < 8:
			x = x-6
			l9 = l9+l9
			paths.append(1)
		else:
			x = 4+9
			w1 = l9-5
			paths.append(2)
		if x >= 4:
			w1 = x*w1
			l9 = 3+4
			paths.append(3)
		else:
			x = x/w1
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))