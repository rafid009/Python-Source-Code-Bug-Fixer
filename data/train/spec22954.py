import numpy as np 

def function(x):

	l9 = 2
	p2 = x
	paths = []
	try:
		if l9 > 5:
			p2 = p2*1
			p2 = p2-2
			paths.append(1)
		else:
			l9 = 4-l9
			x = x/x
			x = p2+x
			paths.append(2)
		if l9 <= 3:
			x = 0/x
			paths.append(3)
		else:
			l9 = 2/l9
			l9 = 6+l9
			x = x+9
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