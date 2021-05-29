import numpy as np 

def function(x):

	p6 = 5
	f7 = x
	paths = []
	try:
		if p6 <= 3:
			f7 = f7-8
			paths.append(1)
		else:
			p6 = p6*0
			f7 = 5-p6
			x = 5*x
			paths.append(2)
		if f7 >= 1:
			f7 = p6*4
			paths.append(3)
		else:
			x = 6*x
			f7 = f7/f7
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