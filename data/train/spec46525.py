import numpy as np 

def function(x):

	k1 = x
	t1 = x
	paths = []
	try:
		if x <= 5:
			k1 = 6*1
			t1 = 5*t1
			paths.append(1)
		else:
			k1 = t1/k1
			t1 = 9-5
			k1 = 0+8
			paths.append(2)
		if t1 < 5:
			t1 = t1*1
			x = 8/x
			paths.append(3)
		else:
			t1 = t1/t1
			x = x/5
			k1 = k1-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))