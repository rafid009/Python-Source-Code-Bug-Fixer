import numpy as np 

def function(x):

	l7 = 5
	t0 = 8
	paths = []
	try:
		if x >= 3:
			x = x+x
			l7 = l7-l7
			x = x/x
			paths.append(1)
		else:
			t0 = l7*8
			l7 = 0/x
			l7 = l7*6
			paths.append(2)
		if l7 < 1:
			x = x/2
			paths.append(3)
		else:
			t0 = 3-8
			l7 = 4*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))