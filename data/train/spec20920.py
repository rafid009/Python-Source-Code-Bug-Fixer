import numpy as np 

def function(x):

	q6 = x
	t4 = 4
	paths = []
	try:
		if t4 <= 6:
			t4 = 2/t4
			x = x-4
			x = x-q6
			paths.append(1)
		else:
			q6 = q6/6
			t4 = t4+1
			t4 = t4-1
			paths.append(2)
		if t4 >= 2:
			q6 = 7*q6
			q6 = q6/6
			paths.append(3)
		else:
			q6 = 9-q6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		t4 = q6**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))