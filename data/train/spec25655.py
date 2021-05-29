import numpy as np 

def function(x):

	t3 = x
	b0 = x
	paths = []
	try:
		if t3 < 3:
			t3 = b0*1
			paths.append(1)
		else:
			b0 = 6+b0
			x = b0-t3
			x = 4/1
			paths.append(2)
		if x < 4:
			x = x-1
			paths.append(3)
		else:
			x = t3+3
			t3 = b0/2
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))