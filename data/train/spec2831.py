import numpy as np 

def function(x):

	i6 = x
	t0 = x
	paths = []
	try:
		if x > 0:
			x = 6+t0
			t0 = 0*t0
			t0 = t0+2
			paths.append(1)
		else:
			i6 = i6*5
			paths.append(2)
		if x < 5:
			x = x/i6
			t0 = i6-9
			paths.append(3)
		else:
			x = 2/x
			x = 6*8
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