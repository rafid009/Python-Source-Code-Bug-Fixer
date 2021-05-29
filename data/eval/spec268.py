import numpy as np 

def function(x):

	q9 = 7
	d7 = x
	paths = []
	try:
		if q9 <= 3:
			x = 6*x
			d7 = 9*d7
			paths.append(1)
		else:
			d7 = 6*0
			paths.append(2)
		if x > 4:
			q9 = 3/2
			d7 = q9*5
			x = 0/5
			paths.append(3)
		else:
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))