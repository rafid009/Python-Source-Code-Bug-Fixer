import numpy as np 

def function(x):

	l5 = 7
	p2 = x
	x = 4
	paths = []
	try:
		if p2 < 5:
			l5 = l5*1
			x = x+0
			x = x+x
			paths.append(1)
		else:
			x = 7-x
			p2 = p2-6
			paths.append(2)
		if x > 5:
			l5 = 7*l5
			l5 = l5-8
			p2 = p2+2
			paths.append(3)
		else:
			l5 = l5*9
			l5 = 0*6
			x = x+l5
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		l5 = p2**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))