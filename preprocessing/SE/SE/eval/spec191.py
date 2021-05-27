import numpy as np 

def function(x):

	b3 = 7
	e2 = 6
	paths = []
	try:
		if x < 5:
			e2 = b3+e2
			e2 = 6+e2
			paths.append(1)
		else:
			e2 = b3*7
			b3 = 6-9
			paths.append(2)
		if b3 < 2:
			e2 = e2/6
			e2 = b3*1
			x = 8+x
			paths.append(3)
		else:
			e2 = 9+b3
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))