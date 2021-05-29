import numpy as np 

def function(x):

	u8 = 0
	t7 = 6
	paths = []
	try:
		if t7 > 2:
			u8 = x*u8
			paths.append(1)
		else:
			x = 3/x
			t7 = x*t7
			u8 = u8+t7
			paths.append(2)
		if t7 >= 1:
			x = 3-5
			t7 = t7+7
			paths.append(3)
		else:
			x = x-t7
			t7 = t7/x
			t7 = 2+t7
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