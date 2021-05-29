import numpy as np 

def function(x):

	f0 = 6
	t1 = x
	paths = []
	try:
		if t1 < 9:
			x = x/x
			x = x*x
			x = x*t1
			paths.append(1)
		else:
			t1 = t1-x
			t1 = t1*8
			t1 = t1-1
			paths.append(2)
		if t1 > 5:
			t1 = t1+7
			paths.append(3)
		else:
			t1 = 5*t1
			t1 = t1-x
			f0 = f0+2
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