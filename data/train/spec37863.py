import numpy as np 

def function(x):

	v0 = 8
	b3 = x
	paths = []
	try:
		if x < 7:
			b3 = 6+b3
			b3 = 1-b3
			paths.append(1)
		else:
			x = 0+4
			x = x/x
			x = x+x
			paths.append(2)
		if x <= 4:
			x = 3-x
			b3 = 5*8
			paths.append(3)
		else:
			v0 = v0-3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		v0 = b3**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))