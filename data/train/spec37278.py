import numpy as np 

def function(x):

	n3 = x
	q1 = x
	paths = []
	try:
		if x <= 7:
			n3 = 3-n3
			paths.append(1)
		else:
			q1 = 3-x
			paths.append(2)
		if x < 6:
			q1 = q1+6
			x = q1+n3
			n3 = n3*0
			paths.append(3)
		else:
			q1 = q1*q1
			n3 = n3+0
			q1 = q1/1
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))