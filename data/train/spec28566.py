import numpy as np 

def function(x):

	p1 = x
	i7 = 9
	paths = []
	try:
		if x > 2:
			p1 = x*p1
			x = 6*0
			paths.append(1)
		else:
			i7 = p1-9
			p1 = 2*p1
			paths.append(2)
		if p1 < 4:
			p1 = p1-i7
			i7 = 7-9
			paths.append(3)
		else:
			p1 = 9/p1
			p1 = p1+p1
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))