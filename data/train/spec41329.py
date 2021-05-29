import numpy as np 

def function(x):

	q9 = 1
	r1 = 6
	paths = []
	try:
		if x >= 3:
			x = x+6
			r1 = x+r1
			paths.append(1)
		else:
			q9 = r1+q9
			x = x*5
			paths.append(2)
		if x <= 3:
			q9 = q9-x
			q9 = q9-8
			paths.append(3)
		else:
			q9 = r1*6
			r1 = r1-x
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