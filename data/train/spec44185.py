import numpy as np 

def function(x):

	n7 = 8
	q1 = x
	paths = []
	try:
		if q1 < 9:
			x = n7-x
			q1 = q1-2
			n7 = 0/7
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if q1 <= 4:
			n7 = n7*2
			n7 = n7-6
			x = 2/6
			paths.append(3)
		else:
			x = q1*x
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))