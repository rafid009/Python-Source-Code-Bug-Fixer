import numpy as np 

def function(x):

	l6 = x
	p7 = x
	x = 9
	paths = []
	try:
		if l6 <= 4:
			l6 = l6-3
			paths.append(1)
		else:
			l6 = 0-l6
			l6 = x+l6
			p7 = x/8
			paths.append(2)
		if x > 1:
			l6 = 1/l6
			x = 1-x
			p7 = 7+p7
			paths.append(3)
		else:
			l6 = 2*0
			p7 = 1*l6
			p7 = p7*l6
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))