import numpy as np 

def function(x):

	t1 = 6
	v9 = 5
	paths = []
	try:
		if v9 < 6:
			x = x/9
			t1 = t1+8
			t1 = 1-7
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if v9 > 4:
			v9 = v9*v9
			t1 = t1*v9
			paths.append(3)
		else:
			v9 = v9-6
			t1 = x-3
			x = t1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))