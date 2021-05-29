import numpy as np 

def function(x):

	q1 = x
	t9 = 1
	paths = []
	try:
		if t9 <= 7:
			q1 = 3/q1
			paths.append(1)
		else:
			x = q1+3
			q1 = 7+4
			paths.append(2)
		if t9 > 0:
			q1 = 0+t9
			x = 5-8
			t9 = t9-9
			paths.append(3)
		else:
			x = 4-x
			t9 = 8/1
			q1 = 0*q1
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))