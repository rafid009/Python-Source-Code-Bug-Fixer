import numpy as np 

def function(x):

	p7 = x
	e9 = x
	paths = []
	try:
		if p7 <= 8:
			p7 = p7/9
			e9 = e9*e9
			e9 = x+e9
			paths.append(1)
		else:
			e9 = 9-6
			x = x+3
			p7 = 4*p7
			paths.append(2)
		if e9 < 3:
			p7 = 3*e9
			paths.append(3)
		else:
			x = 0-5
			p7 = p7+2
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))