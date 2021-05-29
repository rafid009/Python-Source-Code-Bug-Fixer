import numpy as np 

def function(x):

	t8 = 1
	q3 = 3
	paths = []
	try:
		if x < 7:
			q3 = 1+t8
			paths.append(1)
		else:
			q3 = q3/x
			t8 = x+6
			paths.append(2)
		if q3 <= 4:
			x = q3+7
			q3 = 1-q3
			paths.append(3)
		else:
			x = 0-x
			q3 = q3/x
			t8 = 8-5
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))