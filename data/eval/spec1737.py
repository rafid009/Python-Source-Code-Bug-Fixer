import numpy as np 

def function(x):

	f6 = x
	t0 = 7
	paths = []
	try:
		if t0 >= 0:
			f6 = f6/1
			x = x+8
			paths.append(1)
		else:
			f6 = t0/t0
			f6 = 2-f6
			f6 = 1*f6
			paths.append(2)
		if f6 < 9:
			t0 = 0-f6
			x = 7*x
			x = x/6
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))