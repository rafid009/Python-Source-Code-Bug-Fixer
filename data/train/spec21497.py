import numpy as np 

def function(x):

	i2 = 4
	p1 = x
	paths = []
	try:
		if x <= 6:
			x = x+p1
			paths.append(1)
		else:
			i2 = 6-8
			paths.append(2)
		if x > 7:
			i2 = x*6
			p1 = p1/2
			p1 = 3+p1
			paths.append(3)
		else:
			p1 = p1*x
			p1 = 6/x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		p1 = i2**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))