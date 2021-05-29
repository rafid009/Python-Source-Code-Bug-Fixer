import numpy as np 

def function(x):

	v4 = 4
	t7 = x
	paths = []
	try:
		if v4 <= 6:
			t7 = 7/t7
			paths.append(1)
		else:
			x = t7+x
			t7 = t7*x
			paths.append(2)
		if v4 >= 1:
			t7 = t7+9
			paths.append(3)
		else:
			x = t7-0
			v4 = v4+x
			x = x-4
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