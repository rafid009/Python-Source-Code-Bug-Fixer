import numpy as np 

def function(x):

	t9 = x
	r0 = 2
	paths = []
	try:
		if t9 <= 0:
			t9 = t9*6
			paths.append(1)
		else:
			r0 = 7+r0
			r0 = t9/3
			x = x/x
			paths.append(2)
		if t9 < 3:
			t9 = 2-t9
			r0 = 2/r0
			t9 = r0/t9
			paths.append(3)
		else:
			t9 = t9-5
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		r0 = t9**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))