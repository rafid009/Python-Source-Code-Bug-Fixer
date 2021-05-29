import numpy as np 

def function(x):

	w6 = 2
	q4 = x
	paths = []
	try:
		if w6 <= 0:
			x = x+2
			q4 = q4-7
			paths.append(1)
		else:
			x = 0/x
			x = 8/q4
			paths.append(2)
		if w6 < 0:
			q4 = 6+2
			x = 9+x
			paths.append(3)
		else:
			q4 = 5-q4
			w6 = w6/9
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))