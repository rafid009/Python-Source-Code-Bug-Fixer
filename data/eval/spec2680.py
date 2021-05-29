import numpy as np 

def function(x):

	o4 = x
	q7 = 9
	x = x
	paths = []
	try:
		if o4 <= 8:
			o4 = x*o4
			paths.append(1)
		else:
			o4 = 8-o4
			x = x/q7
			q7 = q7*x
			paths.append(2)
		if q7 > 7:
			q7 = q7*x
			paths.append(3)
		else:
			q7 = 3-9
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		q7 = o4**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))