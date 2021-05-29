import numpy as np 

def function(x):

	i0 = 8
	p9 = 7
	paths = []
	try:
		if p9 <= 7:
			i0 = i0+i0
			paths.append(1)
		else:
			i0 = 0*5
			i0 = p9/i0
			paths.append(2)
		if x > 2:
			p9 = i0+p9
			i0 = i0+1
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))