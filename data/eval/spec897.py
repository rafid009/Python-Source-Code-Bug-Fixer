import numpy as np 

def function(x):

	w1 = x
	p9 = 3
	paths = []
	try:
		if p9 >= 8:
			w1 = x-w1
			paths.append(1)
		else:
			w1 = 5*w1
			x = 6-w1
			x = w1-8
			paths.append(2)
		if x >= 3:
			x = x-5
			paths.append(3)
		else:
			x = x+8
			x = x-0
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