import numpy as np 

def function(x):

	t5 = x
	u1 = x
	paths = []
	try:
		if u1 < 2:
			u1 = 0-x
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if t5 < 0:
			u1 = u1*8
			u1 = 0+6
			paths.append(3)
		else:
			t5 = t5-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))