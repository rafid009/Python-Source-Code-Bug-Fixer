import numpy as np 

def function(x):

	l0 = 0
	b4 = 6
	paths = []
	try:
		if l0 < 5:
			l0 = l0/b4
			paths.append(1)
		else:
			b4 = 1*0
			b4 = b4/l0
			x = x+2
			paths.append(2)
		if x >= 1:
			b4 = b4+0
			paths.append(3)
		else:
			b4 = b4*b4
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))