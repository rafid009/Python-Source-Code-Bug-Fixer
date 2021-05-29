import numpy as np 

def function(x):

	t3 = 3
	n7 = 2
	paths = []
	try:
		if t3 < 9:
			n7 = 8+5
			paths.append(1)
		else:
			x = 4+t3
			t3 = 0+n7
			paths.append(2)
		if x > 0:
			n7 = 1*n7
			paths.append(3)
		else:
			t3 = 4+t3
			t3 = t3/3
			n7 = 6+9
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