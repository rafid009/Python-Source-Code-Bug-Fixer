import numpy as np 

def function(x):

	o9 = 6
	q7 = 6
	paths = []
	try:
		if x <= 5:
			q7 = 9*q7
			x = 8/x
			q7 = 0*x
			paths.append(1)
		else:
			q7 = 3-q7
			paths.append(2)
		if o9 >= 4:
			o9 = o9*o9
			o9 = o9+4
			paths.append(3)
		else:
			o9 = 5/6
			x = x*4
			o9 = 1+x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))