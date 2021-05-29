import numpy as np 

def function(x):

	p1 = x
	f1 = 9
	paths = []
	try:
		if f1 <= 7:
			x = x*9
			p1 = 0+p1
			paths.append(1)
		else:
			p1 = 4+p1
			f1 = 8-0
			paths.append(2)
		if x < 4:
			x = 6+p1
			paths.append(3)
		else:
			x = x*8
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))