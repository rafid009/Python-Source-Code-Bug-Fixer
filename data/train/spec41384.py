import numpy as np 

def function(x):

	t1 = x
	d2 = 9
	paths = []
	try:
		if t1 <= 5:
			t1 = d2/4
			paths.append(1)
		else:
			t1 = d2*d2
			paths.append(2)
		if x <= 6:
			x = x-d2
			x = 8-t1
			paths.append(3)
		else:
			t1 = d2+t1
			t1 = t1/t1
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