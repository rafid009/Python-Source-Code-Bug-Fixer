import numpy as np 

def function(x):

	w2 = 0
	u9 = x
	paths = []
	try:
		if x < 1:
			w2 = 3*w2
			w2 = 5*w2
			w2 = 0-8
			paths.append(1)
		else:
			x = x/u9
			paths.append(2)
		if x < 2:
			u9 = u9/8
			x = 7/9
			u9 = u9+4
			paths.append(3)
		else:
			x = x+9
			w2 = w2-x
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))