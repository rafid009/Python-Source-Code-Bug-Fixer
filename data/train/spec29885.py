import numpy as np 

def function(x):

	b4 = x
	q8 = 0
	paths = []
	try:
		if x <= 8:
			q8 = q8-0
			paths.append(1)
		else:
			b4 = b4+7
			b4 = 6+b4
			paths.append(2)
		if b4 >= 8:
			x = 5-x
			b4 = b4*q8
			q8 = q8-8
			paths.append(3)
		else:
			q8 = q8/4
			x = x-0
			x = x-3
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))