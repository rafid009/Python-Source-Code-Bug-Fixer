import numpy as np 

def function(x):

	q1 = 3
	f4 = 9
	x = x
	paths = []
	try:
		if x >= 7:
			f4 = f4-3
			paths.append(1)
		else:
			q1 = q1+5
			q1 = 4-q1
			x = 2-x
			paths.append(2)
		if x < 4:
			f4 = 6-f4
			paths.append(3)
		else:
			f4 = f4/9
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))