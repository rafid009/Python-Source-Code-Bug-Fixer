import numpy as np 

def function(x):

	u0 = 9
	p9 = x
	paths = []
	try:
		if p9 >= 4:
			x = x*1
			p9 = p9/4
			paths.append(1)
		else:
			p9 = 3-u0
			paths.append(2)
		if u0 <= 3:
			u0 = 9-u0
			paths.append(3)
		else:
			x = 5*p9
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