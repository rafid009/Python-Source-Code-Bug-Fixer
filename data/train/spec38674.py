import numpy as np 

def function(x):

	t5 = 7
	k1 = x
	paths = []
	try:
		if k1 > 0:
			t5 = x-7
			paths.append(1)
		else:
			t5 = x*1
			t5 = 1-0
			paths.append(2)
		if k1 < 8:
			t5 = t5*x
			k1 = 2-0
			x = 1-9
			paths.append(3)
		else:
			x = x/3
			k1 = k1+k1
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