import numpy as np 

def function(x):

	b3 = 9
	k0 = x
	paths = []
	try:
		if b3 <= 4:
			x = 2*x
			b3 = 5+b3
			b3 = b3-8
			paths.append(1)
		else:
			b3 = b3/6
			paths.append(2)
		if x < 2:
			b3 = 8-b3
			b3 = 2-b3
			b3 = k0*b3
			paths.append(3)
		else:
			b3 = b3-2
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		b3 = k0**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))