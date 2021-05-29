import numpy as np 

def function(x):

	p2 = 1
	q6 = 1
	paths = []
	try:
		if p2 < 4:
			q6 = q6/9
			p2 = q6+6
			p2 = x/3
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if p2 <= 8:
			x = 6-q6
			p2 = p2+5
			p2 = p2*7
			paths.append(3)
		else:
			p2 = x*4
			x = 7+x
			q6 = 9+8
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))