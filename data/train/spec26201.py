import numpy as np 

def function(x):

	p2 = 8
	y9 = 3
	paths = []
	try:
		if y9 > 7:
			x = y9*0
			paths.append(1)
		else:
			p2 = p2+x
			p2 = y9*p2
			paths.append(2)
		if x > 8:
			x = 7+p2
			p2 = x+p2
			y9 = y9*p2
			paths.append(3)
		else:
			y9 = 7*0
			p2 = p2-2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))