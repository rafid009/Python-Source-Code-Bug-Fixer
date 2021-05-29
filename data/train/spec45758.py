import numpy as np 

def function(x):

	k2 = x
	t1 = x
	paths = []
	try:
		if t1 < 2:
			x = 1*8
			k2 = x-0
			k2 = 1*k2
			paths.append(1)
		else:
			t1 = 6*t1
			k2 = 5-k2
			k2 = k2-t1
			paths.append(2)
		if x > 0:
			x = x*1
			paths.append(3)
		else:
			k2 = k2-6
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))