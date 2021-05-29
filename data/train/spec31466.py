import numpy as np 

def function(x):

	w8 = 1
	e3 = 8
	paths = []
	try:
		if x <= 0:
			x = 1+x
			w8 = x/w8
			paths.append(1)
		else:
			e3 = w8+0
			paths.append(2)
		if e3 > 0:
			x = x/6
			w8 = w8+7
			w8 = w8/x
			paths.append(3)
		else:
			e3 = 9*1
			e3 = 2/e3
			x = 3+5
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))