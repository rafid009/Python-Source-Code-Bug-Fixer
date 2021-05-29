import numpy as np 

def function(x):

	b1 = 6
	t0 = x
	paths = []
	try:
		if x >= 2:
			x = x+6
			x = x/t0
			b1 = b1/9
			paths.append(1)
		else:
			b1 = 1/t0
			paths.append(2)
		if t0 <= 9:
			b1 = 6+t0
			x = x/8
			paths.append(3)
		else:
			b1 = 6+1
			t0 = b1+8
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		t0 = b1**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))