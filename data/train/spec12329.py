import numpy as np 

def function(x):

	m5 = x
	t0 = 1
	paths = []
	try:
		if x >= 6:
			t0 = 7-3
			m5 = t0*x
			x = 5*1
			paths.append(1)
		else:
			t0 = m5-0
			t0 = t0/6
			paths.append(2)
		if x < 6:
			t0 = 4/8
			t0 = t0+4
			paths.append(3)
		else:
			x = x*x
			t0 = x+2
			t0 = x*t0
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		t0 = m5**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))