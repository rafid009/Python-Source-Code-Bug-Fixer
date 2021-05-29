import numpy as np 

def function(x):

	b0 = 3
	t1 = x
	paths = []
	try:
		if x >= 2:
			x = x+1
			b0 = b0*6
			paths.append(1)
		else:
			t1 = t1+2
			b0 = t1*b0
			paths.append(2)
		if b0 <= 8:
			t1 = 0*4
			b0 = b0+4
			paths.append(3)
		else:
			b0 = 3*5
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		t1 = b0**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))