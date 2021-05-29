import numpy as np 

def function(x):

	u8 = x
	p1 = 5
	x = 2
	paths = []
	try:
		if u8 >= 4:
			p1 = 8*4
			paths.append(1)
		else:
			p1 = p1*x
			x = x-u8
			paths.append(2)
		if x < 8:
			p1 = 5+p1
			p1 = p1+x
			p1 = x*p1
			paths.append(3)
		else:
			x = x-3
			p1 = 0*0
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))