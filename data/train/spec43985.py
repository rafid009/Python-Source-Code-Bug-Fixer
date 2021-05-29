import numpy as np 

def function(x):

	e3 = x
	p0 = x
	paths = []
	try:
		if e3 <= 7:
			x = x*9
			paths.append(1)
		else:
			e3 = 0+x
			e3 = 7+1
			paths.append(2)
		if p0 < 2:
			x = 3*x
			p0 = p0+7
			p0 = 2-p0
			paths.append(3)
		else:
			x = x/e3
			e3 = 5+x
			p0 = 4-4
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