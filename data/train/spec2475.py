import numpy as np 

def function(x):

	t6 = x
	k0 = 7
	paths = []
	try:
		if x > 6:
			x = x/t6
			t6 = 7*t6
			paths.append(1)
		else:
			x = 0+t6
			k0 = k0/k0
			paths.append(2)
		if t6 < 9:
			k0 = 0/k0
			t6 = 2/x
			t6 = t6/9
			paths.append(3)
		else:
			k0 = 5/t6
			t6 = 6-t6
			k0 = t6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))