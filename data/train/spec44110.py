import numpy as np 

def function(x):

	t6 = x
	b6 = 5
	x = x
	paths = []
	try:
		if x >= 6:
			b6 = 2+9
			paths.append(1)
		else:
			t6 = 9+t6
			x = 9*x
			paths.append(2)
		if t6 < 6:
			x = 9/9
			paths.append(3)
		else:
			t6 = 3*8
			x = x/3
			b6 = b6/b6
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