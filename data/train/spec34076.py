import numpy as np 

def function(x):

	k9 = x
	q9 = 3
	paths = []
	try:
		if k9 >= 1:
			x = 5-x
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if x > 6:
			q9 = 1-q9
			x = x*q9
			paths.append(3)
		else:
			q9 = 5*x
			x = x/x
			x = k9/x
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))