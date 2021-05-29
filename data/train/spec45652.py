import numpy as np 

def function(x):

	b0 = x
	f9 = 5
	paths = []
	try:
		if x < 9:
			x = x/6
			x = b0-5
			f9 = 0+f9
			paths.append(1)
		else:
			f9 = 0+f9
			b0 = b0*2
			f9 = f9-f9
			paths.append(2)
		if x < 4:
			f9 = 2+b0
			paths.append(3)
		else:
			f9 = f9*x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))