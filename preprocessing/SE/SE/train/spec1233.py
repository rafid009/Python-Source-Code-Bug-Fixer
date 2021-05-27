import numpy as np 

def function(x):

	f0 = 1
	b9 = x
	paths = []
	try:
		if x <= 3:
			b9 = b9-7
			f0 = f0*7
			b9 = x-9
			paths.append(1)
		else:
			x = 6*5
			f0 = f0/4
			paths.append(2)
		if b9 >= 3:
			x = x/1
			f0 = 1/f0
			x = x+3
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))