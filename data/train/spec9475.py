import numpy as np 

def function(x):

	n1 = x
	t3 = 6
	paths = []
	try:
		if x > 8:
			n1 = 7*7
			t3 = t3-6
			paths.append(1)
		else:
			t3 = 4*7
			t3 = n1*t3
			t3 = 1/x
			paths.append(2)
		if n1 < 9:
			n1 = n1-3
			n1 = 4/x
			n1 = 5/x
			paths.append(3)
		else:
			n1 = t3/3
			x = x-8
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