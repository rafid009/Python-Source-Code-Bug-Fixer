import numpy as np 

def function(x):

	q5 = 8
	m2 = x
	paths = []
	try:
		if q5 > 7:
			x = x/x
			paths.append(1)
		else:
			q5 = 8/5
			q5 = x-9
			paths.append(2)
		if q5 < 5:
			q5 = q5+0
			q5 = 2-3
			paths.append(3)
		else:
			q5 = 1-q5
			q5 = 9+q5
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		q5 = m2**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))