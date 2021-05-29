import numpy as np 

def function(x):

	q2 = 5
	v5 = 7
	paths = []
	try:
		if v5 >= 5:
			q2 = q2-5
			q2 = x-q2
			q2 = x*5
			paths.append(1)
		else:
			q2 = v5-0
			paths.append(2)
		if x <= 9:
			x = 4-v5
			paths.append(3)
		else:
			v5 = x+0
			x = 9*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))