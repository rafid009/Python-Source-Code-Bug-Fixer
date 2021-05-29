import numpy as np 

def function(x):

	y3 = 5
	t6 = x
	paths = []
	try:
		if y3 > 1:
			x = x-7
			paths.append(1)
		else:
			y3 = 4-6
			t6 = y3-t6
			t6 = y3/5
			paths.append(2)
		if t6 <= 8:
			x = 4-x
			x = 1-7
			y3 = y3-6
			paths.append(3)
		else:
			y3 = y3+6
			t6 = t6/5
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		t6 = y3**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))