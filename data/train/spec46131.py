import numpy as np 

def function(x):

	q1 = x
	o1 = 7
	paths = []
	try:
		if q1 <= 3:
			q1 = x*2
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if q1 >= 0:
			o1 = 4-2
			q1 = 8+x
			x = x/8
			paths.append(3)
		else:
			o1 = 2*q1
			q1 = o1*1
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