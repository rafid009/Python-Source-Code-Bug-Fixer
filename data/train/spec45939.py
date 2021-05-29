import numpy as np 

def function(x):

	d9 = 7
	q7 = x
	paths = []
	try:
		if d9 < 5:
			d9 = q7-d9
			q7 = q7*5
			paths.append(1)
		else:
			q7 = 2+q7
			paths.append(2)
		if d9 < 3:
			d9 = 5-4
			paths.append(3)
		else:
			d9 = x+d9
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))