import numpy as np 

def function(x):

	l3 = 9
	q1 = x
	paths = []
	try:
		if l3 >= 8:
			q1 = q1+l3
			paths.append(1)
		else:
			q1 = x+q1
			paths.append(2)
		if q1 > 7:
			l3 = 3+l3
			x = l3-5
			q1 = q1*9
			paths.append(3)
		else:
			x = l3*x
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))