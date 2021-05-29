import numpy as np 

def function(x):

	e0 = x
	w2 = x
	paths = []
	try:
		if e0 <= 8:
			x = 1+7
			paths.append(1)
		else:
			x = x+2
			w2 = w2/e0
			w2 = 3-w2
			paths.append(2)
		if x > 5:
			x = 8/9
			e0 = 8+e0
			x = x*7
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))