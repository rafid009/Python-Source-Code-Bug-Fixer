import numpy as np 

def function(x):

	f5 = x
	t4 = 3
	paths = []
	try:
		if x <= 0:
			f5 = x/2
			paths.append(1)
		else:
			x = x-t4
			x = 7/3
			paths.append(2)
		if x <= 0:
			f5 = x*2
			paths.append(3)
		else:
			x = 5*x
			t4 = t4*6
			t4 = t4*t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))