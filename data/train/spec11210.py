import numpy as np 

def function(x):

	t1 = 7
	k9 = 5
	paths = []
	try:
		if x < 6:
			t1 = t1-4
			t1 = 6/6
			paths.append(1)
		else:
			t1 = 2/5
			t1 = x*3
			paths.append(2)
		if x >= 4:
			t1 = 0/x
			t1 = t1-3
			x = k9/x
			paths.append(3)
		else:
			k9 = k9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))