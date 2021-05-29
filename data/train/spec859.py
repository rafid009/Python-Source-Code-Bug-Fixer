import numpy as np 

def function(x):

	t0 = 4
	f9 = 1
	paths = []
	try:
		if t0 <= 1:
			x = x/4
			f9 = 1-f9
			f9 = f9*5
			paths.append(1)
		else:
			t0 = t0-8
			f9 = t0/t0
			x = 1*5
			paths.append(2)
		if t0 < 3:
			f9 = f9+7
			x = t0*x
			f9 = x+x
			paths.append(3)
		else:
			x = x/6
			x = x/8
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		t0 = f9**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))