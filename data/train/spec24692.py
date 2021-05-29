import numpy as np 

def function(x):

	t4 = x
	k3 = x
	paths = []
	try:
		if t4 > 8:
			x = x-8
			k3 = 8-k3
			t4 = t4-2
			paths.append(1)
		else:
			t4 = 2-k3
			k3 = k3-0
			t4 = t4*x
			paths.append(2)
		if x >= 5:
			t4 = 4/t4
			k3 = k3+7
			paths.append(3)
		else:
			t4 = 3-t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))