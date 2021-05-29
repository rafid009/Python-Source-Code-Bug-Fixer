import numpy as np 

def function(x):

	t0 = 0
	f0 = 9
	paths = []
	try:
		if t0 <= 5:
			t0 = t0-5
			paths.append(1)
		else:
			x = x/4
			t0 = 2-0
			t0 = t0/5
			paths.append(2)
		if x >= 8:
			x = t0*2
			x = x-4
			paths.append(3)
		else:
			f0 = f0*x
			f0 = t0+f0
			t0 = 0*t0
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