import numpy as np 

def function(x):

	a7 = x
	p3 = 5
	paths = []
	try:
		if a7 < 7:
			x = x/5
			paths.append(1)
		else:
			x = 2-a7
			paths.append(2)
		if p3 < 2:
			p3 = p3*1
			x = x-3
			paths.append(3)
		else:
			p3 = p3/7
			a7 = x*a7
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		p3 = a7**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))