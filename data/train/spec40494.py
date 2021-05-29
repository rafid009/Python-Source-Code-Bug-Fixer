import numpy as np 

def function(x):

	f0 = x
	t0 = 9
	paths = []
	try:
		if t0 < 6:
			f0 = 9-6
			t0 = 1-9
			f0 = 5-f0
			paths.append(1)
		else:
			x = x/5
			x = x*x
			paths.append(2)
		if f0 >= 7:
			t0 = t0-t0
			f0 = 3-8
			paths.append(3)
		else:
			t0 = t0/8
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))