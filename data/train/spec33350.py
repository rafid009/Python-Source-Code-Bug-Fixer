import numpy as np 

def function(x):

	q6 = x
	d6 = 1
	paths = []
	try:
		if d6 < 5:
			d6 = d6*d6
			q6 = q6-5
			paths.append(1)
		else:
			d6 = 6*9
			paths.append(2)
		if x >= 2:
			x = x+q6
			x = 2*q6
			x = d6-9
			paths.append(3)
		else:
			d6 = d6/d6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		d6 = q6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))