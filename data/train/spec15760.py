import numpy as np 

def function(x):

	b5 = 7
	p9 = 5
	paths = []
	try:
		if p9 <= 7:
			b5 = 4*p9
			paths.append(1)
		else:
			x = x/7
			x = x/x
			paths.append(2)
		if b5 < 9:
			p9 = 5*5
			b5 = 8/b5
			paths.append(3)
		else:
			x = 0+x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))