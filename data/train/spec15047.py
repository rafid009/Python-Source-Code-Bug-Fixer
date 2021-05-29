import numpy as np 

def function(x):

	q8 = x
	l4 = x
	paths = []
	try:
		if x > 4:
			q8 = 3*q8
			paths.append(1)
		else:
			q8 = 8-q8
			l4 = 3*l4
			x = x/2
			paths.append(2)
		if l4 <= 5:
			q8 = 9-1
			l4 = l4*l4
			q8 = q8+3
			paths.append(3)
		else:
			q8 = q8-9
			q8 = q8-5
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