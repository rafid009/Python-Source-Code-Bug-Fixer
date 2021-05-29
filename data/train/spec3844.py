import numpy as np 

def function(x):

	b2 = 6
	f0 = x
	paths = []
	try:
		if b2 <= 9:
			x = x*f0
			paths.append(1)
		else:
			x = x-0
			f0 = f0+2
			b2 = 7*b2
			paths.append(2)
		if x < 9:
			b2 = b2-f0
			f0 = 6-0
			x = 6*b2
			paths.append(3)
		else:
			b2 = 5*b2
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))