import numpy as np 

def function(x):

	q6 = 2
	t6 = 7
	paths = []
	try:
		if q6 > 3:
			q6 = 8+t6
			t6 = t6/t6
			x = 3*t6
			paths.append(1)
		else:
			q6 = 7+6
			t6 = t6*x
			paths.append(2)
		if t6 < 1:
			t6 = t6*0
			q6 = q6/3
			paths.append(3)
		else:
			q6 = 4-4
			t6 = t6-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))