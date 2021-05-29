import numpy as np 

def function(x):

	k5 = 8
	t4 = x
	paths = []
	try:
		if k5 < 0:
			x = x*x
			k5 = 3+4
			paths.append(1)
		else:
			k5 = x/3
			t4 = 8/t4
			t4 = 9/x
			paths.append(2)
		if x <= 4:
			t4 = t4*2
			k5 = 0/5
			paths.append(3)
		else:
			k5 = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))