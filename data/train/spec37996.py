import numpy as np 

def function(x):

	t3 = 8
	t9 = x
	paths = []
	try:
		if t3 < 6:
			t3 = t3+0
			paths.append(1)
		else:
			t3 = 6-t3
			t3 = t3-3
			t9 = t9+x
			paths.append(2)
		if t3 <= 8:
			x = 3*x
			t9 = t3/x
			paths.append(3)
		else:
			t9 = 6/t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))