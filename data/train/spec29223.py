import numpy as np 

def function(x):

	a0 = x
	q8 = x
	paths = []
	try:
		if x >= 3:
			a0 = 1/a0
			a0 = a0/6
			paths.append(1)
		else:
			q8 = q8+0
			x = x*5
			paths.append(2)
		if x < 5:
			x = x/8
			q8 = 6*0
			paths.append(3)
		else:
			a0 = 0/a0
			x = 5-x
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))