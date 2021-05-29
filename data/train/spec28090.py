import numpy as np 

def function(x):

	t4 = x
	w1 = 5
	paths = []
	try:
		if x < 3:
			t4 = x*x
			paths.append(1)
		else:
			x = x+t4
			paths.append(2)
		if t4 <= 7:
			w1 = w1*2
			paths.append(3)
		else:
			x = 8/x
			x = x-3
			x = x-x
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