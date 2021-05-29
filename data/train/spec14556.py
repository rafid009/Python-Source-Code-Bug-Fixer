import numpy as np 

def function(x):

	p2 = x
	f3 = x
	paths = []
	try:
		if x < 7:
			p2 = p2/p2
			p2 = 3+3
			paths.append(1)
		else:
			p2 = 9+0
			x = x/f3
			paths.append(2)
		if p2 <= 4:
			f3 = x-f3
			f3 = 2-2
			paths.append(3)
		else:
			f3 = 1+x
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))