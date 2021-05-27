import numpy as np 

def function(x):

	r1 = 1
	t7 = x
	paths = []
	try:
		if r1 >= 0:
			x = x+3
			t7 = t7+8
			paths.append(1)
		else:
			x = x/2
			t7 = x-t7
			r1 = t7-r1
			paths.append(2)
		if r1 <= 7:
			x = x-2
			paths.append(3)
		else:
			t7 = 9/t7
			x = t7*6
			t7 = t7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))