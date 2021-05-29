import numpy as np 

def function(x):

	b3 = x
	f4 = x
	paths = []
	try:
		if x > 8:
			x = x+5
			x = 7+x
			paths.append(1)
		else:
			x = x*b3
			x = f4+x
			paths.append(2)
		if x < 7:
			f4 = f4-1
			x = 1-5
			b3 = b3/5
			paths.append(3)
		else:
			b3 = 7/b3
			f4 = 4-f4
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))