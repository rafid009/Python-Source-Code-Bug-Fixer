import numpy as np 

def function(x):

	q9 = x
	d2 = 7
	paths = []
	try:
		if x <= 0:
			q9 = 7+q9
			x = 9+x
			d2 = 4+q9
			paths.append(1)
		else:
			d2 = d2+9
			x = x+x
			q9 = q9-5
			paths.append(2)
		if x < 3:
			d2 = 8/d2
			d2 = d2*q9
			paths.append(3)
		else:
			x = d2+2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		q9 = d2**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))