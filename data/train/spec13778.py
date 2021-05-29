import numpy as np 

def function(x):

	d6 = x
	q7 = 9
	x = x
	paths = []
	try:
		if d6 > 2:
			q7 = 6-q7
			paths.append(1)
		else:
			x = x/9
			x = x*6
			paths.append(2)
		if d6 < 8:
			x = d6-9
			q7 = 9-5
			q7 = q7-6
			paths.append(3)
		else:
			x = q7/9
			x = x-4
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		d6 = q7**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))