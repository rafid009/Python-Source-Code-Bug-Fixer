import numpy as np 

def function(x):

	l0 = x
	p6 = 6
	paths = []
	try:
		if p6 <= 2:
			l0 = l0+4
			p6 = p6-x
			p6 = p6/6
			paths.append(1)
		else:
			p6 = p6+9
			paths.append(2)
		if l0 > 4:
			p6 = l0+p6
			x = 5+3
			x = x/3
			paths.append(3)
		else:
			x = x+1
			p6 = p6+3
			l0 = 3-2
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