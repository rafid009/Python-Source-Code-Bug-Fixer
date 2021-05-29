import numpy as np 

def function(x):

	n8 = 7
	q5 = x
	paths = []
	try:
		if q5 < 0:
			n8 = 1-n8
			n8 = n8*n8
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x < 4:
			q5 = 4-q5
			paths.append(3)
		else:
			q5 = q5-7
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))