import numpy as np 

def function(x):

	p3 = 3
	i0 = 1
	paths = []
	try:
		if x >= 0:
			i0 = i0+i0
			x = 6/2
			p3 = x*7
			paths.append(1)
		else:
			x = x*x
			p3 = 5+x
			p3 = 3-p3
			paths.append(2)
		if i0 < 0:
			i0 = 2+8
			x = 8+9
			x = 2*x
			paths.append(3)
		else:
			p3 = p3/x
			p3 = 9*p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		i0 = p3**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))