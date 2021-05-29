import numpy as np 

def function(x):

	b3 = 7
	p9 = x
	paths = []
	try:
		if x <= 5:
			p9 = 3+x
			x = b3/2
			x = x+x
			paths.append(1)
		else:
			x = x/b3
			x = 6-x
			x = x+3
			paths.append(2)
		if x > 8:
			p9 = 9*9
			paths.append(3)
		else:
			b3 = b3+4
			p9 = p9-3
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		b3 = p9**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))