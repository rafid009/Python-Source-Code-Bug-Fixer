import numpy as np 

def function(x):

	t3 = 8
	u2 = 1
	paths = []
	try:
		if u2 >= 3:
			x = x*9
			paths.append(1)
		else:
			t3 = t3/7
			x = x-u2
			paths.append(2)
		if u2 <= 9:
			u2 = 8/u2
			t3 = t3-3
			u2 = u2-2
			paths.append(3)
		else:
			x = 7-t3
			t3 = t3/u2
			u2 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))