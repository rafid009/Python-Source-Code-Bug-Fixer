import numpy as np 

def function(x):

	p9 = x
	b4 = 1
	paths = []
	try:
		if x <= 2:
			p9 = p9/3
			x = p9-x
			paths.append(1)
		else:
			p9 = p9-2
			b4 = b4-7
			x = x+9
			paths.append(2)
		if p9 >= 9:
			x = p9/b4
			p9 = p9/7
			b4 = 0+b4
			paths.append(3)
		else:
			b4 = b4/2
			x = 7-0
			b4 = b4*p9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))