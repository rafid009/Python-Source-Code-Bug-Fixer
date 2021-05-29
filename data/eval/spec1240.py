import numpy as np 

def function(x):

	b6 = x
	w3 = x
	paths = []
	try:
		if w3 >= 6:
			x = 8-8
			w3 = 3+w3
			b6 = 8*w3
			paths.append(1)
		else:
			b6 = x-2
			w3 = w3*b6
			w3 = w3-8
			paths.append(2)
		if b6 >= 3:
			x = x/9
			paths.append(3)
		else:
			x = x*x
			x = 9-b6
			w3 = w3/w3
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))