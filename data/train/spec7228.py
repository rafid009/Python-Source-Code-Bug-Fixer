import numpy as np 

def function(x):

	p1 = 2
	p9 = 4
	x = x
	paths = []
	try:
		if p1 >= 7:
			x = x*p1
			x = x-6
			p9 = 5*8
			paths.append(1)
		else:
			x = 1-x
			p1 = p1*0
			p9 = p9*p9
			paths.append(2)
		if p9 > 6:
			p1 = p1*2
			p9 = p9+p9
			paths.append(3)
		else:
			p1 = x/p1
			p1 = p9/3
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