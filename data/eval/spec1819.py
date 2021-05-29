import numpy as np 

def function(x):

	t0 = x
	b4 = x
	x = 1
	paths = []
	try:
		if x < 9:
			x = 7-x
			b4 = b4+2
			paths.append(1)
		else:
			b4 = b4*t0
			b4 = 0*4
			t0 = t0*x
			paths.append(2)
		if t0 <= 5:
			x = 8-x
			paths.append(3)
		else:
			x = x*7
			b4 = b4/3
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))