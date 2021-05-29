import numpy as np 

def function(x):

	a2 = x
	p9 = 8
	paths = []
	try:
		if a2 >= 8:
			p9 = p9/2
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if p9 < 2:
			x = a2+x
			paths.append(3)
		else:
			p9 = x*x
			a2 = 1+a2
			a2 = a2-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))