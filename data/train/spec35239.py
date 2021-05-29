import numpy as np 

def function(x):

	q8 = 5
	t3 = 1
	paths = []
	try:
		if t3 <= 4:
			t3 = 4-t3
			t3 = 3*t3
			q8 = q8+9
			paths.append(1)
		else:
			q8 = x-9
			q8 = q8*4
			x = 5/x
			paths.append(2)
		if t3 <= 6:
			q8 = q8+t3
			paths.append(3)
		else:
			x = 6/x
			t3 = 9/t3
			q8 = 4-q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))