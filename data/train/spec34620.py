import numpy as np 

def function(x):

	t1 = 4
	q8 = x
	paths = []
	try:
		if q8 > 0:
			x = 9*8
			paths.append(1)
		else:
			x = 5+x
			q8 = q8+q8
			paths.append(2)
		if x > 1:
			t1 = q8+7
			paths.append(3)
		else:
			t1 = 8+t1
			q8 = q8+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))