import numpy as np 

def function(x):

	o7 = x
	q1 = x
	paths = []
	try:
		if o7 < 8:
			o7 = 6-o7
			q1 = 3/9
			paths.append(1)
		else:
			o7 = 5/o7
			paths.append(2)
		if o7 > 4:
			q1 = 2/x
			x = x/q1
			paths.append(3)
		else:
			o7 = x/o7
			x = x*o7
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		q1 = o7**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))