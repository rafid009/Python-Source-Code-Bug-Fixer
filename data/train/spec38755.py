import numpy as np 

def function(x):

	b0 = 7
	p1 = 3
	paths = []
	try:
		if p1 >= 5:
			x = 0*x
			paths.append(1)
		else:
			p1 = p1+5
			paths.append(2)
		if x <= 3:
			p1 = 8*x
			paths.append(3)
		else:
			b0 = b0+b0
			x = x-4
			p1 = b0*1
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))