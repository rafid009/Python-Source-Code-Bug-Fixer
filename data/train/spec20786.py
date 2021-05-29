import numpy as np 

def function(x):

	f6 = 3
	b9 = 2
	paths = []
	try:
		if x > 4:
			f6 = 0+9
			x = x/6
			b9 = b9*1
			paths.append(1)
		else:
			f6 = x*f6
			b9 = 8+f6
			paths.append(2)
		if b9 < 9:
			f6 = f6-2
			x = x+8
			f6 = f6+f6
			paths.append(3)
		else:
			b9 = 5*b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))