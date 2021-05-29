import numpy as np 

def function(x):

	k7 = 2
	b4 = x
	x = x
	paths = []
	try:
		if k7 <= 1:
			k7 = 3/k7
			k7 = 4+k7
			paths.append(1)
		else:
			x = x*2
			b4 = 3+b4
			paths.append(2)
		if b4 < 3:
			k7 = x+k7
			paths.append(3)
		else:
			b4 = 2*b4
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))