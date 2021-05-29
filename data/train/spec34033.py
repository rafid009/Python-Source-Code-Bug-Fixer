import numpy as np 

def function(x):

	q2 = 7
	t4 = x
	paths = []
	try:
		if q2 <= 1:
			t4 = q2/t4
			q2 = t4-q2
			paths.append(1)
		else:
			t4 = x*6
			paths.append(2)
		if q2 < 6:
			q2 = 0/q2
			q2 = 2*q2
			paths.append(3)
		else:
			x = t4*x
			x = 2+9
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))