import numpy as np 

def function(x):

	t0 = 6
	n2 = 8
	paths = []
	try:
		if n2 < 3:
			n2 = n2+5
			t0 = x/n2
			paths.append(1)
		else:
			t0 = t0/t0
			n2 = 9/t0
			paths.append(2)
		if t0 >= 8:
			x = x+2
			n2 = t0+n2
			x = 7*3
			paths.append(3)
		else:
			t0 = x+3
			t0 = t0/x
			x = 1/t0
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