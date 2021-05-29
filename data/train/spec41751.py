import numpy as np 

def function(x):

	b9 = 6
	f7 = 1
	paths = []
	try:
		if x >= 0:
			x = 3+x
			b9 = b9*0
			paths.append(1)
		else:
			f7 = f7+2
			f7 = f7/f7
			b9 = 5/7
			paths.append(2)
		if f7 < 0:
			b9 = b9/3
			b9 = b9-f7
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))