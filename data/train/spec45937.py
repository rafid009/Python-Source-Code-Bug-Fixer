import numpy as np 

def function(x):

	i5 = x
	p3 = 2
	paths = []
	try:
		if i5 <= 4:
			p3 = i5+5
			x = x/9
			p3 = x*p3
			paths.append(1)
		else:
			x = x-x
			x = x*5
			i5 = i5*i5
			paths.append(2)
		if i5 < 1:
			x = 4-9
			p3 = p3/i5
			p3 = p3+p3
			paths.append(3)
		else:
			x = x+i5
			p3 = p3/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))