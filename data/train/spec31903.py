import numpy as np 

def function(x):

	p9 = x
	q1 = x
	paths = []
	try:
		if p9 > 3:
			q1 = q1/5
			paths.append(1)
		else:
			x = 7/x
			q1 = q1*8
			paths.append(2)
		if p9 < 6:
			q1 = 8*q1
			paths.append(3)
		else:
			p9 = p9+p9
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