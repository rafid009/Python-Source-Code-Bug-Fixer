import numpy as np 

def function(x):

	t6 = 2
	y6 = 8
	paths = []
	try:
		if t6 <= 4:
			y6 = 7*5
			t6 = t6/t6
			paths.append(1)
		else:
			t6 = t6-4
			y6 = y6/9
			y6 = 7+t6
			paths.append(2)
		if x >= 8:
			y6 = y6+8
			paths.append(3)
		else:
			y6 = y6/3
			t6 = t6+8
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