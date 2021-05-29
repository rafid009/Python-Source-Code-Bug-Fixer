import numpy as np 

def function(x):

	p1 = 1
	i5 = x
	paths = []
	try:
		if p1 > 2:
			x = 0/x
			p1 = p1/p1
			x = x-x
			paths.append(1)
		else:
			p1 = 4/1
			paths.append(2)
		if p1 < 0:
			i5 = 1+0
			i5 = i5+5
			p1 = 9+i5
			paths.append(3)
		else:
			p1 = 7*p1
			i5 = i5*4
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		p1 = i5**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))