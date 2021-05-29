import numpy as np 

def function(x):

	p3 = x
	f3 = 5
	paths = []
	try:
		if f3 < 4:
			p3 = f3*7
			paths.append(1)
		else:
			f3 = f3*f3
			x = 3-4
			p3 = x+p3
			paths.append(2)
		if p3 <= 1:
			x = 9-f3
			p3 = 7*p3
			paths.append(3)
		else:
			p3 = 3*p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))