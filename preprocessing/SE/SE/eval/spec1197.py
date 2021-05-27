import numpy as np 

def function(x):

	t8 = x
	q2 = 7
	paths = []
	try:
		if q2 < 3:
			q2 = q2*4
			q2 = q2/2
			t8 = 4/1
			paths.append(1)
		else:
			t8 = 8/t8
			paths.append(2)
		if t8 <= 0:
			t8 = 0/t8
			q2 = t8-q2
			paths.append(3)
		else:
			q2 = x+5
			t8 = x/t8
			q2 = 7/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))