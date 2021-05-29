import numpy as np 

def function(x):

	e9 = x
	p1 = x
	paths = []
	try:
		if p1 > 8:
			x = 6+x
			x = 0/1
			e9 = e9-3
			paths.append(1)
		else:
			p1 = 1/9
			p1 = x*p1
			p1 = p1+3
			paths.append(2)
		if x <= 0:
			x = x+p1
			paths.append(3)
		else:
			p1 = p1*3
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