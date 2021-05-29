import numpy as np 

def function(x):

	w6 = x
	b3 = x
	paths = []
	try:
		if b3 >= 3:
			x = x*x
			paths.append(1)
		else:
			x = 6/7
			w6 = w6*7
			paths.append(2)
		if w6 >= 3:
			b3 = 7-b3
			paths.append(3)
		else:
			b3 = 7+2
			w6 = w6-2
			w6 = 6-w6
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