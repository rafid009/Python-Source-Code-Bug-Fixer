import numpy as np 

def function(x):

	t0 = 5
	w4 = x
	paths = []
	try:
		if w4 > 5:
			t0 = x+1
			w4 = w4*w4
			t0 = x*w4
			paths.append(1)
		else:
			t0 = 2/t0
			t0 = 2+t0
			paths.append(2)
		if w4 <= 1:
			t0 = t0*x
			paths.append(3)
		else:
			w4 = 0+w4
			t0 = t0*2
			w4 = w4*1
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