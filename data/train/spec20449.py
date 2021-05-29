import numpy as np 

def function(x):

	t8 = x
	u9 = x
	paths = []
	try:
		if u9 >= 2:
			t8 = 6/u9
			u9 = 3+u9
			paths.append(1)
		else:
			u9 = u9*u9
			u9 = u9-t8
			x = x*x
			paths.append(2)
		if t8 >= 3:
			t8 = t8*t8
			t8 = 0-t8
			x = x*9
			paths.append(3)
		else:
			t8 = 5-t8
			x = x/5
			x = x+x
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		t8 = u9**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))