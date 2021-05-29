import numpy as np 

def function(x):

	q7 = x
	f6 = 3
	paths = []
	try:
		if x < 8:
			f6 = f6-f6
			x = 3+x
			paths.append(1)
		else:
			x = 0+x
			q7 = q7/9
			q7 = 2/x
			paths.append(2)
		if f6 >= 4:
			q7 = q7-2
			q7 = 6/q7
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))