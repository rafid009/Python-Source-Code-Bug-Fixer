import numpy as np 

def function(x):

	l6 = 0
	p8 = x
	paths = []
	try:
		if l6 <= 7:
			p8 = p8*p8
			l6 = 8+l6
			l6 = l6-l6
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if p8 < 2:
			x = x+1
			l6 = l6*6
			x = 2+x
			paths.append(3)
		else:
			p8 = 9-x
			p8 = x+9
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		l6 = p8**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))