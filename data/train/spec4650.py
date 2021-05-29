import numpy as np 

def function(x):

	b8 = x
	w8 = 2
	paths = []
	try:
		if x < 3:
			b8 = x-6
			b8 = 1*b8
			w8 = 4*w8
			paths.append(1)
		else:
			w8 = 8-x
			paths.append(2)
		if w8 <= 4:
			b8 = 0/1
			paths.append(3)
		else:
			x = x-b8
			b8 = b8/4
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		w8 = b8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))