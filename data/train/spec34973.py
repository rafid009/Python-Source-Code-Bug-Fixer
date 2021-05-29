import numpy as np 

def function(x):

	w8 = x
	q4 = 5
	paths = []
	try:
		if x >= 3:
			w8 = w8+7
			paths.append(1)
		else:
			w8 = 9-w8
			x = 0/4
			paths.append(2)
		if q4 > 1:
			w8 = 0+6
			q4 = q4+w8
			w8 = w8-q4
			paths.append(3)
		else:
			q4 = q4/q4
			w8 = 2+1
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))