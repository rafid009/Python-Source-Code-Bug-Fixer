import numpy as np 

def function(x):

	t0 = 8
	x6 = 8
	paths = []
	try:
		if t0 <= 9:
			t0 = t0*1
			x = 5+t0
			t0 = 3*2
			paths.append(1)
		else:
			x6 = x*x6
			x6 = x6*x6
			t0 = t0+1
			paths.append(2)
		if t0 >= 2:
			t0 = t0-x
			t0 = 7/t0
			x6 = x6/6
			paths.append(3)
		else:
			t0 = 4/t0
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