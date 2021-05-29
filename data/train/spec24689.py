import numpy as np 

def function(x):

	l1 = 8
	p8 = x
	paths = []
	try:
		if x > 5:
			x = x-6
			l1 = l1/9
			x = 3*x
			paths.append(1)
		else:
			p8 = 6+x
			p8 = l1/p8
			p8 = p8*4
			paths.append(2)
		if l1 <= 7:
			l1 = 1/5
			p8 = 7+p8
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))