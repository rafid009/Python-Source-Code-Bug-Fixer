import numpy as np 

def function(x):

	t6 = 2
	u4 = 6
	paths = []
	try:
		if x >= 5:
			x = x/6
			u4 = u4/4
			x = x+5
			paths.append(1)
		else:
			u4 = 5-t6
			t6 = t6+t6
			u4 = u4-x
			paths.append(2)
		if t6 >= 4:
			u4 = u4-9
			t6 = t6/6
			x = t6-2
			paths.append(3)
		else:
			t6 = t6-t6
			u4 = u4-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))