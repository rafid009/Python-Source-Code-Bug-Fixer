import numpy as np 

def function(x):

	p2 = x
	r3 = x
	paths = []
	try:
		if p2 < 7:
			r3 = r3/5
			r3 = 1-r3
			paths.append(1)
		else:
			r3 = 4/r3
			p2 = 6+x
			x = x/r3
			paths.append(2)
		if p2 <= 6:
			p2 = 6+x
			r3 = r3*9
			x = x/r3
			paths.append(3)
		else:
			x = x*6
			p2 = x*3
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))