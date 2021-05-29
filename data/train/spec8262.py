import numpy as np 

def function(x):

	a2 = x
	t0 = 9
	paths = []
	try:
		if a2 <= 3:
			t0 = x+3
			paths.append(1)
		else:
			a2 = a2/5
			x = 3*9
			paths.append(2)
		if t0 > 1:
			t0 = t0*7
			t0 = x*3
			paths.append(3)
		else:
			a2 = a2-a2
			a2 = a2*9
			a2 = 7-a2
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