import numpy as np 

def function(x):

	d6 = x
	q5 = x
	paths = []
	try:
		if x >= 3:
			d6 = 4*d6
			x = x*d6
			paths.append(1)
		else:
			q5 = 6/q5
			paths.append(2)
		if x > 8:
			x = x*q5
			paths.append(3)
		else:
			d6 = 2+q5
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))