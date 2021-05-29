import numpy as np 

def function(x):

	p8 = x
	b3 = 2
	paths = []
	try:
		if p8 > 3:
			b3 = 8+b3
			paths.append(1)
		else:
			x = p8+p8
			b3 = b3-9
			paths.append(2)
		if p8 <= 3:
			p8 = p8+7
			x = 5-x
			x = 1+x
			paths.append(3)
		else:
			b3 = 2-x
			b3 = 5+0
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		b3 = p8**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))