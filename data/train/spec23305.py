import numpy as np 

def function(x):

	f8 = x
	t1 = x
	paths = []
	try:
		if t1 > 1:
			x = 7+x
			paths.append(1)
		else:
			t1 = 5*t1
			paths.append(2)
		if f8 > 9:
			x = 0-0
			f8 = 5-x
			x = x/t1
			paths.append(3)
		else:
			x = x*5
			t1 = x/9
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