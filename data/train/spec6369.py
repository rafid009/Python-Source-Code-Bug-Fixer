import numpy as np 

def function(x):

	v8 = x
	p1 = x
	paths = []
	try:
		if v8 > 7:
			x = x-7
			v8 = 6*v8
			paths.append(1)
		else:
			v8 = v8*v8
			x = x*4
			paths.append(2)
		if p1 < 8:
			v8 = 2/8
			v8 = v8+x
			paths.append(3)
		else:
			v8 = v8*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))