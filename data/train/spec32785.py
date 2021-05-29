import numpy as np 

def function(x):

	p6 = 7
	f2 = 0
	paths = []
	try:
		if p6 < 8:
			f2 = f2+6
			p6 = p6+0
			paths.append(1)
		else:
			p6 = p6*x
			paths.append(2)
		if p6 > 9:
			f2 = f2/6
			x = x/f2
			p6 = x/p6
			paths.append(3)
		else:
			f2 = 3*x
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))