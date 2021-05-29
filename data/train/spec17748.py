import numpy as np 

def function(x):

	t1 = x
	y7 = x
	paths = []
	try:
		if y7 <= 7:
			x = y7-4
			x = x/x
			t1 = t1-8
			paths.append(1)
		else:
			t1 = y7*1
			paths.append(2)
		if t1 < 4:
			y7 = y7-x
			paths.append(3)
		else:
			x = 4-y7
			t1 = y7/y7
			t1 = x-6
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		t1 = y7**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))