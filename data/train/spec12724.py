import numpy as np 

def function(x):

	r8 = 9
	t1 = x
	paths = []
	try:
		if x > 1:
			t1 = 7/t1
			paths.append(1)
		else:
			t1 = 5/8
			r8 = r8-r8
			x = x-1
			paths.append(2)
		if x > 9:
			x = t1+5
			x = 8+6
			paths.append(3)
		else:
			r8 = r8-9
			t1 = 9/t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))