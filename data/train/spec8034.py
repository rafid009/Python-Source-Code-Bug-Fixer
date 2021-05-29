import numpy as np 

def function(x):

	p3 = 9
	a1 = x
	paths = []
	try:
		if x <= 8:
			x = x*p3
			x = x-2
			paths.append(1)
		else:
			a1 = a1/1
			p3 = p3+5
			paths.append(2)
		if x >= 8:
			p3 = x-4
			a1 = a1*p3
			paths.append(3)
		else:
			x = x+x
			x = x+4
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		p3 = a1**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))