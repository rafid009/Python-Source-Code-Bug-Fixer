import numpy as np 

def function(x):

	w8 = 2
	p7 = 9
	paths = []
	try:
		if x > 8:
			p7 = x/p7
			paths.append(1)
		else:
			p7 = 6-x
			paths.append(2)
		if w8 > 4:
			w8 = w8-4
			x = 4/x
			w8 = w8/7
			paths.append(3)
		else:
			x = x-7
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		w8 = p7**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))