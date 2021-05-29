import numpy as np 

def function(x):

	q0 = x
	t7 = 8
	paths = []
	try:
		if q0 < 3:
			t7 = t7/8
			x = 5*4
			paths.append(1)
		else:
			x = q0/8
			t7 = t7-7
			paths.append(2)
		if q0 <= 0:
			x = x/7
			q0 = q0-x
			t7 = 1*4
			paths.append(3)
		else:
			t7 = t7/t7
			q0 = q0+q0
			x = q0/4
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		t7 = q0**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))