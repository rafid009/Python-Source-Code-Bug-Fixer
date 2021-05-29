import numpy as np 

def function(x):

	t1 = x
	k1 = x
	paths = []
	try:
		if t1 < 1:
			k1 = t1*k1
			paths.append(1)
		else:
			x = 8-6
			t1 = t1-3
			paths.append(2)
		if x <= 0:
			t1 = t1+x
			paths.append(3)
		else:
			t1 = t1/t1
			k1 = k1+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))