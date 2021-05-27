import numpy as np 

def function(x):

	p4 = 6
	i2 = x
	paths = []
	try:
		if i2 < 9:
			p4 = 8*p4
			i2 = p4/8
			p4 = p4/2
			paths.append(1)
		else:
			p4 = p4+5
			x = 7/9
			p4 = x+i2
			paths.append(2)
		if i2 >= 3:
			p4 = p4-7
			i2 = i2-0
			p4 = 8+x
			paths.append(3)
		else:
			x = i2-2
			x = x-p4
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))