import numpy as np 

def function(x):

	k0 = 8
	q4 = 8
	paths = []
	try:
		if x < 4:
			q4 = x+q4
			paths.append(1)
		else:
			k0 = k0-5
			x = 6/x
			x = x/3
			paths.append(2)
		if x >= 3:
			q4 = q4-6
			q4 = 9-4
			x = 5-x
			paths.append(3)
		else:
			x = x*5
			q4 = q4/k0
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))