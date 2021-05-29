import numpy as np 

def function(x):

	p3 = 1
	j5 = 2
	paths = []
	try:
		if x > 4:
			p3 = j5*p3
			paths.append(1)
		else:
			p3 = p3+0
			p3 = 3*p3
			paths.append(2)
		if p3 >= 1:
			p3 = 2/p3
			j5 = 6*j5
			paths.append(3)
		else:
			p3 = p3-5
			p3 = 7+p3
			p3 = p3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))