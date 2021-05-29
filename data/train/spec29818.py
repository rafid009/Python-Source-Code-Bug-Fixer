import numpy as np 

def function(x):

	t9 = 4
	q2 = 0
	paths = []
	try:
		if q2 < 9:
			q2 = 3-q2
			t9 = 5/9
			q2 = q2+9
			paths.append(1)
		else:
			t9 = q2*t9
			paths.append(2)
		if x < 0:
			q2 = 2-8
			t9 = x+0
			x = x+x
			paths.append(3)
		else:
			t9 = t9-x
			t9 = q2-q2
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