import numpy as np 

def function(x):

	f4 = 1
	b2 = 1
	x = x
	paths = []
	try:
		if b2 > 2:
			b2 = x+9
			x = f4-x
			paths.append(1)
		else:
			x = 2+x
			f4 = x*4
			b2 = b2/8
			paths.append(2)
		if b2 > 8:
			x = 5*x
			f4 = 0+3
			paths.append(3)
		else:
			b2 = b2+f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))