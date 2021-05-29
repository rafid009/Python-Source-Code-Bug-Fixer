import numpy as np 

def function(x):

	t1 = 5
	t9 = 1
	paths = []
	try:
		if x < 7:
			t9 = t9-3
			t9 = 4/2
			x = 1*x
			paths.append(1)
		else:
			t9 = t1+t9
			t9 = 1/t9
			paths.append(2)
		if t1 < 7:
			t1 = t1/t1
			x = 4+x
			paths.append(3)
		else:
			t1 = t1*9
			t1 = x+t1
			t9 = t9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))