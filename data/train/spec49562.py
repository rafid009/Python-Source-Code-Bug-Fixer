import numpy as np 

def function(x):

	m1 = 6
	w8 = x
	paths = []
	try:
		if w8 > 7:
			x = 9/4
			paths.append(1)
		else:
			m1 = 2-4
			w8 = 2-w8
			paths.append(2)
		if w8 <= 5:
			x = w8/8
			x = 7-x
			paths.append(3)
		else:
			w8 = w8/9
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