import numpy as np 

def function(x):

	q4 = x
	d9 = x
	paths = []
	try:
		if q4 <= 7:
			x = 9*x
			q4 = q4*5
			paths.append(1)
		else:
			x = d9+x
			paths.append(2)
		if x > 2:
			x = x/6
			q4 = x/9
			paths.append(3)
		else:
			d9 = d9-0
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		q4 = d9**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))