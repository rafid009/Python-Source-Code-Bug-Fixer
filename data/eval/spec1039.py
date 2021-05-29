import numpy as np 

def function(x):

	w6 = x
	q1 = 9
	paths = []
	try:
		if q1 <= 3:
			x = 4/x
			w6 = 7+q1
			paths.append(1)
		else:
			x = x*3
			x = x*7
			paths.append(2)
		if x < 2:
			x = 3/q1
			q1 = 7*q1
			paths.append(3)
		else:
			q1 = w6-q1
			w6 = 9/w6
			x = x/4
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))