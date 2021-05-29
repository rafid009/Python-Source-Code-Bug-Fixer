import numpy as np 

def function(x):

	k3 = 7
	t6 = 8
	paths = []
	try:
		if x > 5:
			x = k3*9
			t6 = t6/2
			k3 = k3-9
			paths.append(1)
		else:
			x = x/x
			k3 = 5+k3
			paths.append(2)
		if x < 6:
			t6 = t6*x
			k3 = k3-4
			paths.append(3)
		else:
			x = k3+9
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))