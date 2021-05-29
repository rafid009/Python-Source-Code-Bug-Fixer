import numpy as np 

def function(x):

	t7 = x
	paths = []
	try:
		if t7 >= 9:
			t7 = t7-1
			t7 = t7/3
			t7 = t7/t7
			paths.append(1)
		else:
			x = x/t7
			paths.append(2)
		if t7 >= 7:
			t7 = x/t7
			paths.append(3)
		else:
			t7 = t7-4
			t7 = 4/t7
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