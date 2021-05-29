import numpy as np 

def function(x):

	f8 = x
	p8 = 9
	paths = []
	try:
		if p8 <= 2:
			p8 = 2+p8
			f8 = f8+x
			x = x*p8
			paths.append(1)
		else:
			p8 = 3*p8
			x = 2+x
			paths.append(2)
		if x >= 0:
			p8 = 8*p8
			p8 = p8-p8
			f8 = p8/6
			paths.append(3)
		else:
			f8 = 6*5
			x = f8/x
			x = x-6
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