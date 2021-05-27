import numpy as np 

def function(x):

	b2 = x
	v1 = x
	paths = []
	try:
		if x >= 9:
			x = b2/b2
			paths.append(1)
		else:
			b2 = 6/5
			paths.append(2)
		if x >= 8:
			v1 = 0-v1
			x = 8-2
			x = 5*8
			paths.append(3)
		else:
			b2 = b2-b2
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		b2 = v1**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))