import numpy as np 

def function(x):

	f6 = x
	b2 = 4
	paths = []
	try:
		if f6 <= 0:
			x = x/2
			paths.append(1)
		else:
			f6 = 5/f6
			b2 = f6+b2
			paths.append(2)
		if x <= 4:
			f6 = x-f6
			x = 5*x
			b2 = b2*5
			paths.append(3)
		else:
			x = 2/2
			x = x-x
			b2 = b2+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))