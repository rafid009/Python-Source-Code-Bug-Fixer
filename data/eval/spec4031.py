import numpy as np 

def function(x):

	t7 = 2
	r0 = x
	paths = []
	try:
		if x >= 7:
			r0 = t7-9
			r0 = 8/7
			paths.append(1)
		else:
			r0 = 1-2
			t7 = t7/1
			t7 = x+t7
			paths.append(2)
		if x >= 4:
			r0 = r0*6
			r0 = r0-0
			paths.append(3)
		else:
			t7 = t7-9
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