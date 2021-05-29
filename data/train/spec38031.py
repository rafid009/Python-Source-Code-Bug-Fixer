import numpy as np 

def function(x):

	y8 = 2
	t0 = x
	paths = []
	try:
		if y8 >= 1:
			x = 6+4
			t0 = t0+7
			t0 = t0/5
			paths.append(1)
		else:
			t0 = 6+t0
			paths.append(2)
		if x <= 1:
			x = x*x
			x = x/x
			t0 = t0*2
			paths.append(3)
		else:
			x = 8*x
			y8 = 1/1
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