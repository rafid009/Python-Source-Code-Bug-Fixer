import numpy as np 

def function(x):

	t0 = 5
	p2 = x
	x = 5
	paths = []
	try:
		if p2 >= 9:
			t0 = t0*t0
			paths.append(1)
		else:
			x = 5/t0
			p2 = p2/4
			x = 3-2
			paths.append(2)
		if p2 < 5:
			x = 7-6
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		t0 = p2**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))