import numpy as np 

def function(x):

	b0 = x
	a0 = 9
	paths = []
	try:
		if b0 <= 8:
			b0 = b0-a0
			a0 = 2-3
			x = x+4
			paths.append(1)
		else:
			a0 = a0*9
			x = 2*a0
			b0 = 3/3
			paths.append(2)
		if b0 > 4:
			a0 = a0*3
			x = 4/5
			b0 = 3-b0
			paths.append(3)
		else:
			b0 = x+b0
			b0 = a0-2
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))