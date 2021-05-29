import numpy as np 

def function(x):

	m1 = 3
	t2 = 0
	paths = []
	try:
		if x > 6:
			m1 = 3*t2
			t2 = 9/2
			paths.append(1)
		else:
			t2 = t2+x
			t2 = 7*3
			paths.append(2)
		if m1 < 9:
			m1 = x-1
			paths.append(3)
		else:
			t2 = 2-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))