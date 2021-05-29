import numpy as np 

def function(x):

	p0 = 6
	i5 = 6
	paths = []
	try:
		if x > 0:
			p0 = p0-i5
			i5 = x+i5
			x = 9+x
			paths.append(1)
		else:
			p0 = 4*i5
			i5 = i5/i5
			paths.append(2)
		if i5 <= 1:
			x = 2*x
			p0 = p0+x
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		i5 = p0**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))