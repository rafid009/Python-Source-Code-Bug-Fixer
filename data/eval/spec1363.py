import numpy as np 

def function(x):

	u0 = x
	p8 = 8
	paths = []
	try:
		if p8 >= 9:
			x = x/2
			p8 = x+p8
			paths.append(1)
		else:
			p8 = 9*3
			paths.append(2)
		if u0 > 7:
			x = 4/1
			paths.append(3)
		else:
			p8 = p8/6
			p8 = p8*0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		p8 = u0**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))