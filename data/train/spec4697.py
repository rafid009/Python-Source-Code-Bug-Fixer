import numpy as np 

def function(x):

	u3 = 6
	p3 = x
	x = x
	paths = []
	try:
		if x < 3:
			u3 = 5+7
			paths.append(1)
		else:
			p3 = 5*x
			x = 3+2
			paths.append(2)
		if p3 >= 8:
			u3 = u3*p3
			paths.append(3)
		else:
			p3 = p3+5
			u3 = p3-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))