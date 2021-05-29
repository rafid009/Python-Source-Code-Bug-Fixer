import numpy as np 

def function(x):

	v3 = 3
	b0 = 3
	paths = []
	try:
		if b0 <= 4:
			b0 = 7+x
			paths.append(1)
		else:
			v3 = v3-9
			paths.append(2)
		if v3 >= 6:
			b0 = b0/6
			b0 = v3/1
			b0 = 8-3
			paths.append(3)
		else:
			b0 = 4+6
			b0 = x*b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		v3 = b0**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))