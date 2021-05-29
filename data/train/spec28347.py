import numpy as np 

def function(x):

	f2 = 5
	p0 = x
	paths = []
	try:
		if x >= 9:
			f2 = 2+f2
			paths.append(1)
		else:
			f2 = p0-f2
			f2 = 7*0
			paths.append(2)
		if f2 < 6:
			f2 = 8+p0
			paths.append(3)
		else:
			x = p0*9
			p0 = p0+x
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