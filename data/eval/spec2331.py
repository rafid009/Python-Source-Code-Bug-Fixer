import numpy as np 

def function(x):

	i1 = 3
	p8 = 7
	paths = []
	try:
		if x > 9:
			x = i1*0
			p8 = x*0
			paths.append(1)
		else:
			p8 = i1/1
			paths.append(2)
		if i1 > 6:
			p8 = 0*p8
			p8 = p8*4
			i1 = 5-i1
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))