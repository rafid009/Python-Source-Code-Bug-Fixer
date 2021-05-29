import numpy as np 

def function(x):

	b7 = 4
	r0 = x
	paths = []
	try:
		if b7 >= 7:
			b7 = 1+b7
			x = 0+x
			paths.append(1)
		else:
			b7 = b7+2
			r0 = b7*x
			x = 8/x
			paths.append(2)
		if r0 < 3:
			b7 = r0-2
			b7 = 9-b7
			paths.append(3)
		else:
			b7 = b7+4
			b7 = 8+b7
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		b7 = r0**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))