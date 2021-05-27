import numpy as np 

def function(x):

	e7 = x
	t5 = 3
	paths = []
	try:
		if e7 < 1:
			t5 = 0-t5
			paths.append(1)
		else:
			x = x-7
			t5 = 7-5
			t5 = 0/t5
			paths.append(2)
		if e7 <= 6:
			e7 = 2*e7
			t5 = t5+6
			x = x-0
			paths.append(3)
		else:
			x = t5*9
			x = e7+e7
			e7 = 0+7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))