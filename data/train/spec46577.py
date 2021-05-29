import numpy as np 

def function(x):

	f8 = 3
	g1 = 2
	paths = []
	try:
		if x >= 7:
			f8 = g1/f8
			paths.append(1)
		else:
			f8 = f8+g1
			x = x+x
			g1 = g1/1
			paths.append(2)
		if x > 4:
			x = g1-x
			x = g1+x
			paths.append(3)
		else:
			x = x*1
			x = g1*g1
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