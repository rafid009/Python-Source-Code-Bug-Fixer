import numpy as np 

def function(x):

	l3 = x
	p8 = 5
	paths = []
	try:
		if x > 7:
			p8 = 9+p8
			paths.append(1)
		else:
			p8 = 2+p8
			paths.append(2)
		if p8 <= 0:
			p8 = p8*2
			paths.append(3)
		else:
			l3 = 1*l3
			p8 = l3/3
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))