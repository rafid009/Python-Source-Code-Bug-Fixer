import numpy as np 

def function(x):

	r5 = 3
	q7 = x
	paths = []
	try:
		if r5 >= 9:
			q7 = 1-q7
			x = 5+x
			paths.append(1)
		else:
			q7 = q7*r5
			q7 = q7/5
			q7 = q7+2
			paths.append(2)
		if x > 9:
			r5 = 8*5
			paths.append(3)
		else:
			r5 = q7+2
			r5 = r5+r5
			q7 = q7-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))