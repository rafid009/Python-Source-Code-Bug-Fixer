import numpy as np 

def function(x):

	t9 = x
	u9 = x
	paths = []
	try:
		if t9 <= 9:
			t9 = t9*3
			u9 = 5/u9
			paths.append(1)
		else:
			u9 = t9+u9
			u9 = 8*8
			t9 = x/8
			paths.append(2)
		if t9 < 1:
			t9 = 5/t9
			t9 = t9+5
			t9 = t9-6
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		t9 = u9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))