import numpy as np 

def function(x):

	k3 = 7
	t7 = 3
	x = x
	paths = []
	try:
		if k3 > 3:
			t7 = t7*x
			k3 = 2/x
			x = 8-x
			paths.append(1)
		else:
			t7 = t7*x
			paths.append(2)
		if k3 >= 6:
			k3 = k3-t7
			paths.append(3)
		else:
			t7 = 3*t7
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		t7 = k3**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))