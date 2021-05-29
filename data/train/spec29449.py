import numpy as np 

def function(x):

	q2 = x
	o2 = x
	x = x
	paths = []
	try:
		if o2 > 7:
			x = x-1
			q2 = 4/q2
			paths.append(1)
		else:
			o2 = o2/o2
			paths.append(2)
		if o2 <= 8:
			o2 = 9/o2
			q2 = 9/1
			x = 4*x
			paths.append(3)
		else:
			o2 = 4-3
			x = 9-x
			q2 = q2/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))