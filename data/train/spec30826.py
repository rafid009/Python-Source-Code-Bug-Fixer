import numpy as np 

def function(x):

	b6 = 5
	p8 = 2
	paths = []
	try:
		if p8 <= 2:
			x = x-7
			paths.append(1)
		else:
			p8 = p8*x
			b6 = b6+2
			b6 = b6-0
			paths.append(2)
		if x <= 2:
			x = x-6
			p8 = b6-9
			x = x/4
			paths.append(3)
		else:
			x = x*3
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		b6 = p8**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))