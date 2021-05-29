import numpy as np 

def function(x):

	q2 = x
	t9 = x
	paths = []
	try:
		if t9 <= 0:
			q2 = q2+8
			paths.append(1)
		else:
			t9 = t9*1
			paths.append(2)
		if q2 < 5:
			q2 = t9*q2
			t9 = 8*t9
			paths.append(3)
		else:
			q2 = 4-q2
			q2 = 3-8
			t9 = t9+x
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))