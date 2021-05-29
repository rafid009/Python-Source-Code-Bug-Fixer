import numpy as np 

def function(x):

	p4 = 4
	p1 = x
	x = 1
	paths = []
	try:
		if x <= 3:
			p1 = p1+4
			x = x*0
			paths.append(1)
		else:
			p4 = p4*x
			paths.append(2)
		if x < 4:
			p1 = p1+p1
			x = 7*1
			paths.append(3)
		else:
			x = x/4
			p1 = 2*p1
			p1 = 6/p1
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))