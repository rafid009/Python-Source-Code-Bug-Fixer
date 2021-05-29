import numpy as np 

def function(x):

	p8 = 4
	e3 = 1
	paths = []
	try:
		if x <= 4:
			x = x*4
			paths.append(1)
		else:
			p8 = 6*9
			paths.append(2)
		if e3 > 3:
			e3 = e3+e3
			p8 = p8/x
			paths.append(3)
		else:
			e3 = x/1
			x = 7+e3
			e3 = 2-e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		p8 = e3**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))