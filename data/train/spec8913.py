import numpy as np 

def function(x):

	f3 = 7
	p3 = x
	paths = []
	try:
		if x >= 9:
			p3 = p3-8
			paths.append(1)
		else:
			f3 = p3+9
			x = f3*x
			paths.append(2)
		if f3 < 2:
			x = x*8
			paths.append(3)
		else:
			p3 = p3+9
			f3 = 2-f3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))