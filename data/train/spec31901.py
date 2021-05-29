import numpy as np 

def function(x):

	f5 = 6
	b3 = 1
	paths = []
	try:
		if b3 > 8:
			x = 7/8
			x = 1/x
			x = x+9
			paths.append(1)
		else:
			x = x*8
			b3 = 5*b3
			paths.append(2)
		if f5 > 1:
			b3 = b3*x
			paths.append(3)
		else:
			b3 = f5*7
			f5 = f5*f5
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		f5 = b3**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))