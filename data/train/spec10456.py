import numpy as np 

def function(x):

	q7 = 4
	w6 = x
	x = 0
	paths = []
	try:
		if w6 < 2:
			w6 = 9-1
			paths.append(1)
		else:
			q7 = q7*1
			w6 = w6-9
			paths.append(2)
		if w6 > 0:
			q7 = 7*q7
			w6 = x+w6
			x = 4-x
			paths.append(3)
		else:
			w6 = 1+w6
			x = x/1
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))