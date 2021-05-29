import numpy as np 

def function(x):

	i6 = 6
	p9 = 2
	paths = []
	try:
		if p9 > 2:
			x = p9-3
			paths.append(1)
		else:
			x = p9/x
			p9 = p9+0
			x = 4*x
			paths.append(2)
		if i6 <= 3:
			p9 = x/2
			paths.append(3)
		else:
			i6 = 9+x
			i6 = 8*i6
			p9 = p9-3
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))