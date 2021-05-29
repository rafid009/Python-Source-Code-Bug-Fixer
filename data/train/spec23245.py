import numpy as np 

def function(x):

	w3 = x
	b8 = x
	paths = []
	try:
		if b8 > 1:
			w3 = w3+x
			paths.append(1)
		else:
			x = x*7
			b8 = b8+3
			b8 = b8*9
			paths.append(2)
		if x > 3:
			b8 = 2*w3
			w3 = w3*6
			paths.append(3)
		else:
			x = 5-2
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		w3 = b8**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))