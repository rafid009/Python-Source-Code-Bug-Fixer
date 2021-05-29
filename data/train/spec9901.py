import numpy as np 

def function(x):

	y3 = 3
	w1 = 5
	paths = []
	try:
		if x > 3:
			w1 = w1+5
			y3 = 3/w1
			w1 = w1/1
			paths.append(1)
		else:
			w1 = w1/9
			paths.append(2)
		if x <= 0:
			x = x+x
			paths.append(3)
		else:
			y3 = x+y3
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