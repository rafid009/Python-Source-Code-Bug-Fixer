import numpy as np 

def function(x):

	q3 = x
	t1 = 6
	paths = []
	try:
		if q3 < 0:
			t1 = 2*2
			t1 = 2-t1
			paths.append(1)
		else:
			x = 4/7
			paths.append(2)
		if t1 <= 9:
			t1 = t1/9
			x = 9/3
			paths.append(3)
		else:
			t1 = 3-t1
			q3 = q3-x
			q3 = 4+6
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