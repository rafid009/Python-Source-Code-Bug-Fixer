import numpy as np 

def function(x):

	q8 = 0
	n7 = x
	paths = []
	try:
		if x < 2:
			x = x+6
			paths.append(1)
		else:
			n7 = x-8
			n7 = n7+5
			q8 = 7-q8
			paths.append(2)
		if n7 <= 4:
			x = 9+0
			q8 = 8+q8
			q8 = n7+q8
			paths.append(3)
		else:
			x = x-5
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