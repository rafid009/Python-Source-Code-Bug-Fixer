import numpy as np 

def function(x):

	d1 = x
	q5 = 1
	paths = []
	try:
		if d1 >= 4:
			x = q5/q5
			q5 = d1/q5
			d1 = 6+3
			paths.append(1)
		else:
			d1 = d1-1
			paths.append(2)
		if q5 >= 4:
			q5 = 4+q5
			paths.append(3)
		else:
			d1 = d1/x
			q5 = 8+x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))