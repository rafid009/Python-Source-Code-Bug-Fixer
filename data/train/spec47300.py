import numpy as np 

def function(x):

	t3 = 0
	v7 = x
	paths = []
	try:
		if t3 <= 9:
			t3 = 8/2
			v7 = 3*v7
			x = 0-t3
			paths.append(1)
		else:
			t3 = 8*v7
			paths.append(2)
		if v7 >= 1:
			v7 = 3+t3
			x = t3-x
			paths.append(3)
		else:
			t3 = 0*t3
			x = v7+2
			t3 = t3/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))