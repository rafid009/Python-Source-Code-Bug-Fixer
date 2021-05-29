import numpy as np 

def function(x):

	t2 = x
	u4 = 7
	paths = []
	try:
		if x <= 4:
			u4 = 2-u4
			u4 = u4+8
			u4 = 4*u4
			paths.append(1)
		else:
			t2 = t2*5
			paths.append(2)
		if u4 >= 9:
			x = 9/x
			t2 = u4-t2
			paths.append(3)
		else:
			u4 = u4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))