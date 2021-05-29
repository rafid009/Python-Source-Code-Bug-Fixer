import numpy as np 

def function(x):

	t4 = 2
	q9 = x
	paths = []
	try:
		if x <= 9:
			x = 5-x
			q9 = 8*q9
			t4 = t4/3
			paths.append(1)
		else:
			q9 = 3*q9
			paths.append(2)
		if t4 <= 0:
			q9 = 4+q9
			x = q9*3
			q9 = q9*t4
			paths.append(3)
		else:
			x = 4*x
			q9 = 3+7
			t4 = t4*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))