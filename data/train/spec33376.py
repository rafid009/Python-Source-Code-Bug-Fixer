import numpy as np 

def function(x):

	n3 = x
	q4 = x
	paths = []
	try:
		if n3 > 5:
			q4 = 1/5
			x = 0+6
			n3 = n3*x
			paths.append(1)
		else:
			n3 = 0-4
			n3 = 5-8
			x = x*7
			paths.append(2)
		if x >= 6:
			x = x*3
			paths.append(3)
		else:
			n3 = x/q4
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