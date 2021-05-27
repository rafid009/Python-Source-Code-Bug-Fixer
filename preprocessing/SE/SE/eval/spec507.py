import numpy as np 

def function(x):

	j9 = 6
	p2 = 7
	paths = []
	try:
		if p2 < 9:
			x = 0+x
			paths.append(1)
		else:
			p2 = j9+2
			j9 = 7-x
			j9 = j9+0
			paths.append(2)
		if j9 > 6:
			x = 2-j9
			p2 = 6+6
			x = x/6
			paths.append(3)
		else:
			p2 = 0-5
			p2 = p2*8
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