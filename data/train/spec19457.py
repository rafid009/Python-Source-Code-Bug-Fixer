import numpy as np 

def function(x):

	w1 = x
	e7 = x
	x = 2
	paths = []
	try:
		if e7 < 8:
			x = x*1
			paths.append(1)
		else:
			x = 3-1
			x = 4/e7
			paths.append(2)
		if x <= 1:
			e7 = e7+e7
			paths.append(3)
		else:
			w1 = w1-1
			x = x-8
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