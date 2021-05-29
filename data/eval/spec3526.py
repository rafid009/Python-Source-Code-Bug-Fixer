import numpy as np 

def function(x):

	w5 = x
	l8 = 4
	paths = []
	try:
		if w5 >= 5:
			w5 = 2+w5
			w5 = w5+1
			w5 = 4/7
			paths.append(1)
		else:
			x = w5*4
			l8 = x/2
			paths.append(2)
		if l8 < 0:
			w5 = x+w5
			x = 5+x
			paths.append(3)
		else:
			l8 = l8*l8
			l8 = 7-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))