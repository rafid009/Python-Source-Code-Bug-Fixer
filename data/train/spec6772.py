import numpy as np 

def function(x):

	t3 = 3
	p4 = 0
	paths = []
	try:
		if p4 > 0:
			p4 = 7*p4
			p4 = t3-0
			p4 = p4+2
			paths.append(1)
		else:
			t3 = 8*t3
			x = 3+x
			paths.append(2)
		if p4 > 7:
			x = 5-x
			t3 = t3/x
			paths.append(3)
		else:
			t3 = 0-1
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