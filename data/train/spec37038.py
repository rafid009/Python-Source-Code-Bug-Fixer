import numpy as np 

def function(x):

	t9 = 9
	t0 = x
	paths = []
	try:
		if t9 > 2:
			t9 = t0-7
			x = x*2
			paths.append(1)
		else:
			t9 = x*t9
			t0 = 7+4
			paths.append(2)
		if t0 < 1:
			t0 = t0-t0
			t0 = t0/x
			paths.append(3)
		else:
			x = 3-t9
			x = x*1
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))