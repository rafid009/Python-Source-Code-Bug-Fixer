import numpy as np 

def function(x):

	w2 = x
	l1 = 6
	paths = []
	try:
		if x <= 3:
			l1 = w2*8
			w2 = w2-8
			paths.append(1)
		else:
			l1 = w2-x
			paths.append(2)
		if l1 > 7:
			w2 = w2*6
			w2 = w2-1
			x = x/6
			paths.append(3)
		else:
			w2 = 1*w2
			l1 = 4/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))