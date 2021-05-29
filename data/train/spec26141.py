import numpy as np 

def function(x):

	p3 = 9
	i4 = 8
	paths = []
	try:
		if i4 <= 4:
			i4 = i4*i4
			p3 = 6/7
			x = x+x
			paths.append(1)
		else:
			p3 = 3*i4
			p3 = 9-i4
			paths.append(2)
		if p3 > 1:
			i4 = 6*i4
			paths.append(3)
		else:
			x = x/9
			i4 = x*i4
			i4 = i4/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))