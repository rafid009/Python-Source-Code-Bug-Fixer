import numpy as np 

def function(x):

	s4 = 7
	p3 = x
	x = x
	paths = []
	try:
		if s4 > 8:
			p3 = 9-p3
			p3 = p3+9
			x = p3*7
			paths.append(1)
		else:
			x = x-x
			x = x/1
			paths.append(2)
		if x > 1:
			p3 = x*0
			paths.append(3)
		else:
			x = x-4
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