import numpy as np 

def function(x):

	w2 = x
	d1 = x
	paths = []
	try:
		if d1 >= 2:
			d1 = d1/5
			x = 7-x
			paths.append(1)
		else:
			x = 1/3
			x = 6*x
			paths.append(2)
		if x > 6:
			x = d1-x
			x = 8+x
			paths.append(3)
		else:
			x = x*w2
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