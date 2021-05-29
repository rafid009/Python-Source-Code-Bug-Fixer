import numpy as np 

def function(x):

	p2 = x
	f0 = 1
	paths = []
	try:
		if f0 > 4:
			f0 = 6*9
			paths.append(1)
		else:
			p2 = p2*5
			f0 = x-f0
			x = 7+x
			paths.append(2)
		if f0 <= 0:
			p2 = p2/p2
			x = x+3
			paths.append(3)
		else:
			p2 = 9+f0
			f0 = 3+f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		p2 = f0**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))