import numpy as np 

def function(x):

	b6 = 8
	y2 = x
	paths = []
	try:
		if x < 5:
			b6 = 7*x
			paths.append(1)
		else:
			x = x-5
			b6 = 6/y2
			paths.append(2)
		if y2 >= 4:
			b6 = b6+y2
			paths.append(3)
		else:
			x = x*6
			b6 = 0*2
			x = b6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))