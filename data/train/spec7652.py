import numpy as np 

def function(x):

	t8 = 4
	t1 = 1
	paths = []
	try:
		if t1 < 0:
			t8 = t8-6
			x = 7-x
			paths.append(1)
		else:
			t1 = 0/x
			t1 = x+t1
			paths.append(2)
		if t1 <= 3:
			t8 = 7*t8
			paths.append(3)
		else:
			t1 = 2+t8
			x = 1+t8
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))