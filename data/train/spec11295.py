import numpy as np 

def function(x):

	f8 = x
	p8 = 8
	paths = []
	try:
		if x > 4:
			x = p8/x
			x = p8*x
			f8 = 8*3
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if p8 < 6:
			p8 = p8/p8
			p8 = 5-f8
			paths.append(3)
		else:
			x = x+5
			p8 = p8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))