import numpy as np 

def function(x):

	p1 = x
	f5 = x
	paths = []
	try:
		if f5 >= 8:
			f5 = f5/8
			paths.append(1)
		else:
			x = f5/2
			p1 = 2*p1
			f5 = f5/8
			paths.append(2)
		if f5 >= 4:
			p1 = p1-6
			f5 = 7-x
			paths.append(3)
		else:
			p1 = p1+x
			x = 2*x
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))