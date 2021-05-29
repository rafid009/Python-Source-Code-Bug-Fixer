import numpy as np 

def function(x):

	b6 = x
	e2 = x
	paths = []
	try:
		if x >= 6:
			e2 = 8*e2
			x = x+b6
			b6 = 7*b6
			paths.append(1)
		else:
			e2 = e2+b6
			paths.append(2)
		if e2 >= 0:
			x = x+3
			e2 = e2+1
			x = x*b6
			paths.append(3)
		else:
			b6 = 9+x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))