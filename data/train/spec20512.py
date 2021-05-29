import numpy as np 

def function(x):

	p4 = 8
	f3 = 4
	paths = []
	try:
		if p4 > 7:
			x = x*p4
			p4 = 7/p4
			paths.append(1)
		else:
			x = x/5
			f3 = 3+p4
			p4 = 5-1
			paths.append(2)
		if f3 < 0:
			f3 = f3-3
			f3 = 8/f3
			paths.append(3)
		else:
			p4 = p4/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))