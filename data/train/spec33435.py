import numpy as np 

def function(x):

	u9 = 6
	t9 = 9
	paths = []
	try:
		if t9 > 3:
			u9 = x+x
			paths.append(1)
		else:
			t9 = t9/4
			t9 = t9/8
			x = u9-2
			paths.append(2)
		if u9 >= 0:
			u9 = u9*7
			paths.append(3)
		else:
			t9 = 9/1
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))