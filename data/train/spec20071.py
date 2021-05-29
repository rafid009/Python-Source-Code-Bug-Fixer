import numpy as np 

def function(x):

	b2 = x
	v1 = 8
	paths = []
	try:
		if x >= 2:
			x = 9+4
			v1 = 7*b2
			paths.append(1)
		else:
			x = x/9
			b2 = b2*5
			paths.append(2)
		if v1 >= 8:
			v1 = 5-v1
			paths.append(3)
		else:
			v1 = b2*x
			v1 = 3-2
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