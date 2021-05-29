import numpy as np 

def function(x):

	p7 = 3
	t1 = x
	paths = []
	try:
		if p7 < 9:
			t1 = 5-0
			t1 = 9+7
			paths.append(1)
		else:
			t1 = 4*t1
			t1 = 6/t1
			paths.append(2)
		if p7 >= 3:
			t1 = t1/2
			x = x-1
			paths.append(3)
		else:
			p7 = 8-p7
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