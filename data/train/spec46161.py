import numpy as np 

def function(x):

	w1 = x
	x9 = 1
	x = 0
	paths = []
	try:
		if w1 > 8:
			x9 = 2+x9
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if x9 <= 5:
			w1 = w1-x
			w1 = w1+w1
			x9 = x9+8
			paths.append(3)
		else:
			x9 = x9+4
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))