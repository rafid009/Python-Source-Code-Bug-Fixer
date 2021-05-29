import numpy as np 

def function(x):

	q8 = x
	b7 = 5
	paths = []
	try:
		if x < 8:
			b7 = 4-b7
			x = x+1
			b7 = 1/b7
			paths.append(1)
		else:
			x = 9-q8
			paths.append(2)
		if b7 > 2:
			q8 = 3/q8
			paths.append(3)
		else:
			b7 = 4-6
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