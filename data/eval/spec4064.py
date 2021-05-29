import numpy as np 

def function(x):

	t9 = 5
	k5 = 6
	paths = []
	try:
		if x < 5:
			k5 = 2/k5
			paths.append(1)
		else:
			t9 = 1-x
			paths.append(2)
		if k5 > 2:
			k5 = 7-5
			k5 = k5-2
			paths.append(3)
		else:
			t9 = t9*5
			k5 = 6-9
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))