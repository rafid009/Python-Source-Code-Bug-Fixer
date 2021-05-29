import numpy as np 

def function(x):

	v0 = 7
	t3 = x
	paths = []
	try:
		if x < 1:
			t3 = t3/x
			x = x-1
			t3 = t3+t3
			paths.append(1)
		else:
			x = 4/x
			paths.append(2)
		if x < 0:
			t3 = 5/4
			v0 = v0-9
			v0 = 6*v0
			paths.append(3)
		else:
			v0 = v0*5
			v0 = 5/t3
			v0 = v0+x
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