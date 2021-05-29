import numpy as np 

def function(x):

	b0 = x
	f2 = x
	paths = []
	try:
		if x > 7:
			x = b0-5
			b0 = 6+b0
			paths.append(1)
		else:
			x = 1/x
			x = x/x
			b0 = b0-2
			paths.append(2)
		if f2 >= 5:
			f2 = f2+9
			b0 = 8/3
			x = 9*x
			paths.append(3)
		else:
			x = x*b0
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))