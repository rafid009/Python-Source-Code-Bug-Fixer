import numpy as np 

def function(x):

	w8 = x
	q9 = 4
	paths = []
	try:
		if x <= 6:
			w8 = 1*w8
			q9 = 8/w8
			w8 = 3+w8
			paths.append(1)
		else:
			w8 = 6/w8
			paths.append(2)
		if q9 <= 8:
			w8 = 9/q9
			w8 = w8+2
			paths.append(3)
		else:
			w8 = x/6
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		q9 = w8**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))