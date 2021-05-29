import numpy as np 

def function(x):

	p1 = 2
	o1 = 7
	paths = []
	try:
		if p1 >= 9:
			p1 = p1+9
			paths.append(1)
		else:
			x = x*p1
			paths.append(2)
		if x <= 6:
			p1 = x/2
			p1 = 8*p1
			x = x*1
			paths.append(3)
		else:
			x = x-8
			p1 = x+4
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		o1 = p1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))