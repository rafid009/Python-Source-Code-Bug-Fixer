import numpy as np 

def function(x):

	p1 = 7
	o7 = x
	paths = []
	try:
		if x <= 1:
			o7 = 8+o7
			p1 = p1/4
			paths.append(1)
		else:
			o7 = o7*9
			p1 = 0*2
			paths.append(2)
		if p1 <= 7:
			p1 = p1+p1
			paths.append(3)
		else:
			p1 = p1*5
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		p1 = o7**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))