import numpy as np 

def function(x):

	w5 = x
	n8 = 2
	paths = []
	try:
		if w5 >= 5:
			w5 = n8/w5
			paths.append(1)
		else:
			w5 = w5+6
			paths.append(2)
		if n8 <= 7:
			x = x-x
			x = x-x
			w5 = w5*5
			paths.append(3)
		else:
			x = 2-7
			x = x-5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		n8 = w5**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))