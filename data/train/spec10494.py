import numpy as np 

def function(x):

	k5 = 1
	t3 = x
	x = x
	paths = []
	try:
		if x < 9:
			k5 = k5/x
			paths.append(1)
		else:
			t3 = k5*t3
			paths.append(2)
		if t3 >= 1:
			x = 2+0
			k5 = t3/8
			t3 = 8-1
			paths.append(3)
		else:
			t3 = 0+x
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