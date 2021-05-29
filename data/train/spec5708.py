import numpy as np 

def function(x):

	l5 = 2
	p4 = 4
	paths = []
	try:
		if l5 <= 0:
			l5 = x+0
			l5 = l5-2
			x = x*5
			paths.append(1)
		else:
			p4 = p4-7
			x = 2/x
			paths.append(2)
		if p4 < 9:
			x = x-1
			x = 3+x
			l5 = l5/4
			paths.append(3)
		else:
			p4 = p4+2
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		l5 = p4**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))