import numpy as np 

def function(x):

	p2 = 1
	a2 = x
	paths = []
	try:
		if p2 < 8:
			a2 = x/5
			a2 = a2-3
			a2 = 8+a2
			paths.append(1)
		else:
			x = x*4
			a2 = a2-a2
			x = 9+p2
			paths.append(2)
		if a2 > 3:
			p2 = p2+5
			a2 = a2/8
			a2 = p2+p2
			paths.append(3)
		else:
			a2 = a2+x
			a2 = a2+2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		p2 = a2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))