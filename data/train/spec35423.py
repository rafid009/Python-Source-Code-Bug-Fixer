import numpy as np 

def function(x):

	u1 = 8
	t6 = 1
	paths = []
	try:
		if u1 >= 4:
			t6 = t6*t6
			t6 = t6+4
			t6 = x*8
			paths.append(1)
		else:
			x = 4/u1
			u1 = 2/u1
			x = u1*8
			paths.append(2)
		if t6 >= 3:
			u1 = u1*1
			u1 = 4/u1
			paths.append(3)
		else:
			u1 = t6*u1
			t6 = t6/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))