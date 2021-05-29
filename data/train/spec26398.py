import numpy as np 

def function(x):

	p9 = x
	y9 = x
	paths = []
	try:
		if y9 < 8:
			y9 = y9*p9
			y9 = 4+x
			x = x*4
			paths.append(1)
		else:
			p9 = x*1
			p9 = 3+p9
			paths.append(2)
		if p9 > 0:
			p9 = 7+p9
			paths.append(3)
		else:
			p9 = p9/1
			x = x/9
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