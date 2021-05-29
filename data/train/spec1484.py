import numpy as np 

def function(x):

	q1 = x
	n7 = 1
	x = x
	paths = []
	try:
		if x < 6:
			n7 = q1-x
			paths.append(1)
		else:
			x = x*5
			q1 = x*q1
			n7 = n7*9
			paths.append(2)
		if n7 <= 4:
			q1 = 8+x
			n7 = 3-n7
			n7 = n7/4
			paths.append(3)
		else:
			n7 = n7+8
			x = x*7
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