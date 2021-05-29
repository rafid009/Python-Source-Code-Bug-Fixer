import numpy as np 

def function(x):

	t0 = 5
	i7 = 9
	paths = []
	try:
		if t0 > 1:
			i7 = t0*i7
			t0 = i7-i7
			x = 3/x
			paths.append(1)
		else:
			t0 = 9/i7
			x = 3+x
			x = x+4
			paths.append(2)
		if x <= 1:
			t0 = t0+2
			i7 = i7*3
			i7 = 9-x
			paths.append(3)
		else:
			i7 = 9-4
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