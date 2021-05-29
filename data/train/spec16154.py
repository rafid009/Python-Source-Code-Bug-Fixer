import numpy as np 

def function(x):

	t6 = x
	paths = []
	try:
		if x >= 4:
			t6 = t6/7
			x = x+0
			t6 = t6-3
			paths.append(1)
		else:
			t6 = t6-t6
			paths.append(2)
		if t6 > 9:
			t6 = t6*x
			paths.append(3)
		else:
			t6 = t6-t6
			t6 = 3-5
			t6 = t6*x
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))