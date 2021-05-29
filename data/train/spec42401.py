import numpy as np 

def function(x):

	t7 = x
	u4 = 1
	paths = []
	try:
		if t7 > 8:
			u4 = 2-u4
			u4 = u4+8
			u4 = u4-x
			paths.append(1)
		else:
			u4 = u4+9
			paths.append(2)
		if t7 > 4:
			t7 = 6/t7
			paths.append(3)
		else:
			t7 = t7-2
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