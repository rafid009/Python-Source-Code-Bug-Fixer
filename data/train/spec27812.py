import numpy as np 

def function(x):

	k8 = 9
	t4 = 3
	paths = []
	try:
		if t4 <= 9:
			x = x+6
			x = x*k8
			paths.append(1)
		else:
			t4 = t4*4
			k8 = k8-2
			paths.append(2)
		if t4 <= 7:
			x = x/5
			k8 = 6/t4
			paths.append(3)
		else:
			k8 = k8+7
			k8 = 6-k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))