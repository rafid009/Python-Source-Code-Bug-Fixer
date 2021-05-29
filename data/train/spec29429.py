import numpy as np 

def function(x):

	t0 = x
	v7 = 1
	x = x
	paths = []
	try:
		if v7 <= 2:
			v7 = t0+1
			t0 = 0+7
			paths.append(1)
		else:
			x = x/9
			t0 = 7*t0
			x = x-x
			paths.append(2)
		if t0 >= 0:
			x = x*v7
			t0 = v7/4
			paths.append(3)
		else:
			v7 = v7/3
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		v7 = t0**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))