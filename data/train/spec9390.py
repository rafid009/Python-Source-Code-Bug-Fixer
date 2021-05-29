import numpy as np 

def function(x):

	e3 = x
	b3 = 6
	paths = []
	try:
		if e3 >= 4:
			b3 = b3/7
			paths.append(1)
		else:
			b3 = b3+x
			paths.append(2)
		if e3 <= 8:
			x = 8-x
			x = x+b3
			e3 = 6+e3
			paths.append(3)
		else:
			b3 = 4-b3
			x = 6/b3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))