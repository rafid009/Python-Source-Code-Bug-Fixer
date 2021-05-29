import numpy as np 

def function(x):

	w8 = 2
	q5 = x
	paths = []
	try:
		if q5 > 3:
			q5 = 1+w8
			q5 = q5/2
			x = x+x
			paths.append(1)
		else:
			q5 = 5/q5
			w8 = w8-q5
			w8 = w8-9
			paths.append(2)
		if q5 <= 8:
			w8 = 3/4
			x = x+8
			paths.append(3)
		else:
			w8 = 4+3
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