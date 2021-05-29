import numpy as np 

def function(x):

	t0 = 4
	i7 = 9
	paths = []
	try:
		if t0 >= 4:
			x = 5-9
			t0 = 3*1
			x = x/1
			paths.append(1)
		else:
			t0 = t0/9
			paths.append(2)
		if i7 < 5:
			t0 = t0+8
			paths.append(3)
		else:
			t0 = x*i7
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))