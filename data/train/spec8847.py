import numpy as np 

def function(x):

	t6 = x
	q8 = x
	paths = []
	try:
		if x >= 9:
			t6 = t6*q8
			paths.append(1)
		else:
			x = 3+1
			t6 = t6+t6
			q8 = q8*7
			paths.append(2)
		if x > 8:
			q8 = q8-7
			t6 = 4+8
			paths.append(3)
		else:
			x = q8*x
			t6 = t6+5
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		t6 = q8**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))