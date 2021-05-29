import numpy as np 

def function(x):

	j5 = x
	p1 = 7
	paths = []
	try:
		if p1 <= 2:
			x = x+1
			p1 = 4+p1
			paths.append(1)
		else:
			p1 = p1-9
			x = x+9
			paths.append(2)
		if j5 <= 4:
			p1 = p1/3
			paths.append(3)
		else:
			j5 = x-2
			x = 3/5
			j5 = 4*p1
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