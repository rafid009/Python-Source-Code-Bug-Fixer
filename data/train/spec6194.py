import numpy as np 

def function(x):

	u2 = 6
	t1 = 2
	paths = []
	try:
		if x >= 4:
			x = x/4
			paths.append(1)
		else:
			u2 = 0+u2
			u2 = u2*t1
			t1 = t1*0
			paths.append(2)
		if x > 4:
			x = 8*t1
			u2 = t1/2
			paths.append(3)
		else:
			x = 1/x
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