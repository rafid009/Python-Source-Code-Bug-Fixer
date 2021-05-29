import numpy as np 

def function(x):

	r7 = 8
	q1 = x
	paths = []
	try:
		if x < 1:
			x = x/2
			q1 = 4-r7
			paths.append(1)
		else:
			r7 = r7+r7
			q1 = 7-q1
			paths.append(2)
		if r7 > 5:
			r7 = r7-7
			q1 = q1/x
			paths.append(3)
		else:
			q1 = 2+8
			q1 = 9*q1
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		r7 = q1**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))