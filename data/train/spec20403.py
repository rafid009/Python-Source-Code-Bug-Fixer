import numpy as np 

def function(x):

	x1 = x
	w2 = 9
	paths = []
	try:
		if x1 < 4:
			x = 2/w2
			w2 = 6-w2
			x = w2/1
			paths.append(1)
		else:
			x = x1*x
			paths.append(2)
		if x1 <= 0:
			x1 = x1/4
			x1 = 7+x1
			paths.append(3)
		else:
			w2 = w2*w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))