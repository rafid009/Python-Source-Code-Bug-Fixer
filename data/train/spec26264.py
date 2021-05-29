import numpy as np 

def function(x):

	q1 = x
	a3 = 4
	paths = []
	try:
		if a3 <= 3:
			a3 = a3+a3
			x = q1+x
			paths.append(1)
		else:
			x = a3-x
			a3 = a3*a3
			a3 = 3/a3
			paths.append(2)
		if a3 >= 6:
			a3 = q1-x
			a3 = a3/3
			a3 = a3+9
			paths.append(3)
		else:
			x = x*6
			q1 = x/6
			a3 = 1+q1
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