import numpy as np 

def function(x):

	k8 = x
	t6 = 7
	paths = []
	try:
		if k8 < 1:
			k8 = 3*t6
			t6 = 9-t6
			paths.append(1)
		else:
			x = k8/x
			paths.append(2)
		if t6 >= 0:
			x = x+x
			t6 = 9/t6
			paths.append(3)
		else:
			t6 = 4/5
			t6 = t6-5
			t6 = t6-x
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