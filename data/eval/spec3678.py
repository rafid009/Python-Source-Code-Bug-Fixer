import numpy as np 

def function(x):

	b2 = 6
	w5 = 1
	paths = []
	try:
		if x < 5:
			b2 = 7-x
			paths.append(1)
		else:
			w5 = w5+w5
			paths.append(2)
		if x >= 0:
			x = x+9
			b2 = w5/5
			b2 = b2/b2
			paths.append(3)
		else:
			b2 = x/b2
			b2 = 9-b2
			w5 = w5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))