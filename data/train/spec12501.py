import numpy as np 

def function(x):

	t2 = x
	t0 = 5
	paths = []
	try:
		if t0 < 3:
			t2 = 8*t2
			paths.append(1)
		else:
			t0 = t0/t0
			t0 = t0*x
			paths.append(2)
		if t2 > 7:
			t0 = t0*1
			t2 = t2+x
			t2 = 5*t2
			paths.append(3)
		else:
			t2 = t2*4
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))