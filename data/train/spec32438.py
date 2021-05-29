import numpy as np 

def function(x):

	t6 = 3
	t7 = x
	paths = []
	try:
		if x >= 9:
			t6 = 0+t6
			x = 1-x
			t7 = x*2
			paths.append(1)
		else:
			t6 = t7+6
			paths.append(2)
		if t6 > 8:
			t7 = 7/t7
			t7 = 5-t7
			x = 0+8
			paths.append(3)
		else:
			t7 = t7/t6
			x = x+4
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