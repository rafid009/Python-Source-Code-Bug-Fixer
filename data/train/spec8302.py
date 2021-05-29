import numpy as np 

def function(x):

	r4 = x
	t9 = 1
	paths = []
	try:
		if t9 >= 4:
			r4 = 2-r4
			x = x-9
			x = x-4
			paths.append(1)
		else:
			r4 = 6*x
			t9 = 1*r4
			paths.append(2)
		if x > 8:
			r4 = r4+3
			t9 = 1/t9
			paths.append(3)
		else:
			t9 = 1*6
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		t9 = r4**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))