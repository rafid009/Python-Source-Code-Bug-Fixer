import numpy as np 

def function(x):

	w4 = 4
	b1 = 3
	paths = []
	try:
		if b1 <= 5:
			b1 = b1-0
			w4 = 1*w4
			paths.append(1)
		else:
			b1 = b1*0
			w4 = 5+w4
			x = 8*w4
			paths.append(2)
		if x >= 6:
			b1 = b1-4
			x = x*w4
			paths.append(3)
		else:
			x = b1-w4
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		w4 = b1**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))