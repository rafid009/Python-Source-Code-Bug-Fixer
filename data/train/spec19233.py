import numpy as np 

def function(x):

	t7 = 2
	y5 = x
	x = 8
	paths = []
	try:
		if y5 < 2:
			y5 = 3+y5
			t7 = t7*1
			t7 = 4-2
			paths.append(1)
		else:
			x = 3+3
			x = x-1
			x = 4/x
			paths.append(2)
		if y5 <= 7:
			x = 3/x
			y5 = y5+y5
			t7 = x*x
			paths.append(3)
		else:
			x = t7-6
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