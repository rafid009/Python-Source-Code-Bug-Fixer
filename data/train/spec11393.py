import numpy as np 

def function(x):

	k4 = x
	p1 = x
	paths = []
	try:
		if x > 5:
			x = x*4
			p1 = p1+p1
			paths.append(1)
		else:
			p1 = k4-5
			p1 = 5+p1
			paths.append(2)
		if k4 <= 4:
			k4 = k4-5
			k4 = x+k4
			paths.append(3)
		else:
			p1 = p1*5
			x = 1+x
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