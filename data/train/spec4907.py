import numpy as np 

def function(x):

	q1 = x
	p3 = x
	paths = []
	try:
		if x > 0:
			p3 = 8/p3
			q1 = 3+p3
			x = 9-x
			paths.append(1)
		else:
			q1 = q1*p3
			x = x/q1
			x = x*3
			paths.append(2)
		if q1 >= 4:
			x = 8-p3
			paths.append(3)
		else:
			p3 = 3/3
			p3 = 8-0
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		q1 = p3**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))