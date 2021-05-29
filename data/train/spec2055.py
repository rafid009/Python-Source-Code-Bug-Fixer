import numpy as np 

def function(x):

	t9 = 2
	q3 = x
	x = 6
	paths = []
	try:
		if q3 <= 6:
			q3 = q3+8
			q3 = 1*5
			q3 = q3+9
			paths.append(1)
		else:
			x = 7-x
			q3 = x-9
			t9 = 7/3
			paths.append(2)
		if t9 <= 0:
			q3 = 9-q3
			x = x+x
			paths.append(3)
		else:
			x = x/6
			x = x+7
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		t9 = q3**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))