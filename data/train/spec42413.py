import numpy as np 

def function(x):

	u4 = 7
	t2 = x
	paths = []
	try:
		if t2 > 9:
			u4 = u4/9
			paths.append(1)
		else:
			x = x/6
			x = t2-2
			paths.append(2)
		if u4 > 0:
			u4 = u4*5
			paths.append(3)
		else:
			t2 = x*t2
			t2 = t2-t2
			t2 = 4*t2
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