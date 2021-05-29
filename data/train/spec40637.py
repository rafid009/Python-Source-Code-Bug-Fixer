import numpy as np 

def function(x):

	b8 = x
	w9 = 3
	paths = []
	try:
		if b8 >= 9:
			b8 = x/b8
			x = x/1
			paths.append(1)
		else:
			b8 = 4/b8
			paths.append(2)
		if b8 < 6:
			w9 = 2/w9
			w9 = 2*b8
			paths.append(3)
		else:
			b8 = w9-7
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		w9 = b8**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))