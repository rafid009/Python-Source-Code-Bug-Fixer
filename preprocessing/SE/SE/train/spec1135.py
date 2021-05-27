import numpy as np 

def function(x):

	b3 = x
	w4 = x
	paths = []
	try:
		if b3 < 3:
			w4 = 6/w4
			paths.append(1)
		else:
			x = x-b3
			paths.append(2)
		if w4 <= 9:
			w4 = w4+w4
			w4 = w4-6
			x = b3+x
			paths.append(3)
		else:
			w4 = 3-8
			b3 = b3+4
			b3 = b3+7
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))