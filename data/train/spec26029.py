import numpy as np 

def function(x):

	e3 = x
	p1 = x
	paths = []
	try:
		if p1 <= 5:
			p1 = 0+7
			p1 = p1+6
			p1 = p1+p1
			paths.append(1)
		else:
			e3 = e3/9
			x = 9*9
			paths.append(2)
		if e3 < 4:
			p1 = 1/p1
			x = 5-3
			p1 = 1+7
			paths.append(3)
		else:
			p1 = p1/2
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))