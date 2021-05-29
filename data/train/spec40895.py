import numpy as np 

def function(x):

	u3 = 1
	t0 = x
	paths = []
	try:
		if t0 < 8:
			u3 = 0+u3
			paths.append(1)
		else:
			t0 = t0*5
			t0 = 6-t0
			paths.append(2)
		if u3 < 7:
			x = t0+u3
			x = 7*x
			x = x/9
			paths.append(3)
		else:
			t0 = 5*t0
			u3 = 1+u3
			t0 = t0*7
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))