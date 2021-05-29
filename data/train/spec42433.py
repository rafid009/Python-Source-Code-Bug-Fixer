import numpy as np 

def function(x):

	t5 = 5
	k5 = x
	paths = []
	try:
		if t5 <= 2:
			k5 = 0+k5
			k5 = k5*4
			k5 = k5/x
			paths.append(1)
		else:
			k5 = 3+k5
			paths.append(2)
		if t5 < 7:
			t5 = 5*9
			k5 = 7-k5
			k5 = k5*1
			paths.append(3)
		else:
			k5 = k5-t5
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