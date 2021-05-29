import numpy as np 

def function(x):

	l9 = x
	p9 = x
	paths = []
	try:
		if l9 > 1:
			p9 = l9/7
			p9 = p9*x
			x = p9/x
			paths.append(1)
		else:
			x = x/p9
			paths.append(2)
		if x > 7:
			x = 2*x
			x = x/3
			p9 = l9+p9
			paths.append(3)
		else:
			l9 = p9-2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		l9 = p9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))