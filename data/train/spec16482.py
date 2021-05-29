import numpy as np 

def function(x):

	r8 = 7
	p8 = 2
	paths = []
	try:
		if x < 8:
			r8 = 9/r8
			x = x+8
			paths.append(1)
		else:
			p8 = p8*p8
			r8 = r8+x
			paths.append(2)
		if r8 <= 7:
			p8 = p8-6
			x = 5+r8
			paths.append(3)
		else:
			p8 = x/3
			p8 = r8*x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))