import numpy as np 

def function(x):

	w8 = 9
	l6 = 0
	paths = []
	try:
		if l6 <= 7:
			w8 = 7+w8
			x = 8+x
			paths.append(1)
		else:
			x = 1*x
			x = 3+x
			x = x+x
			paths.append(2)
		if x > 2:
			l6 = l6+w8
			w8 = w8*1
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))