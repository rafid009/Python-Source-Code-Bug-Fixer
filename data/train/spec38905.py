import numpy as np 

def function(x):

	t7 = 9
	d8 = 9
	paths = []
	try:
		if t7 > 5:
			x = 5/x
			t7 = 4*t7
			paths.append(1)
		else:
			x = x+7
			t7 = x*t7
			paths.append(2)
		if t7 < 3:
			x = x-t7
			x = 6-t7
			paths.append(3)
		else:
			d8 = d8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))