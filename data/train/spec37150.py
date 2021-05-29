import numpy as np 

def function(x):

	b2 = 7
	w9 = x
	paths = []
	try:
		if w9 > 4:
			b2 = b2-x
			w9 = w9+w9
			paths.append(1)
		else:
			x = 1*6
			b2 = x/5
			paths.append(2)
		if x <= 0:
			x = x-6
			paths.append(3)
		else:
			b2 = 5-8
			x = x/6
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))