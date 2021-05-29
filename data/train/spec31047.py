import numpy as np 

def function(x):

	e8 = x
	t7 = 3
	paths = []
	try:
		if t7 <= 0:
			t7 = 7+t7
			paths.append(1)
		else:
			t7 = t7/6
			t7 = 8-1
			t7 = 8+t7
			paths.append(2)
		if e8 <= 1:
			t7 = e8/t7
			paths.append(3)
		else:
			x = t7/e8
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))