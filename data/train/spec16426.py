import numpy as np 

def function(x):

	p7 = 9
	a7 = x
	x = 7
	paths = []
	try:
		if p7 > 5:
			x = x-9
			paths.append(1)
		else:
			x = p7-5
			a7 = 2+a7
			paths.append(2)
		if a7 <= 0:
			p7 = p7/5
			x = x*7
			paths.append(3)
		else:
			a7 = a7-2
			x = x*8
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		p7 = a7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))