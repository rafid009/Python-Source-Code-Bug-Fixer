import numpy as np 

def function(x):

	p3 = 2
	f0 = 1
	paths = []
	try:
		if p3 < 5:
			p3 = x-2
			p3 = p3+0
			x = x+0
			paths.append(1)
		else:
			p3 = p3*0
			p3 = x+7
			paths.append(2)
		if f0 > 5:
			f0 = x/f0
			paths.append(3)
		else:
			x = 6+p3
			x = 3*1
			x = p3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))