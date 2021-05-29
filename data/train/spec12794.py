import numpy as np 

def function(x):

	v8 = x
	p0 = 2
	x = x
	paths = []
	try:
		if x <= 0:
			x = x+7
			paths.append(1)
		else:
			p0 = p0+3
			p0 = 2-p0
			paths.append(2)
		if p0 > 3:
			v8 = 8*v8
			p0 = 7*1
			v8 = v8/3
			paths.append(3)
		else:
			x = x+4
			x = x*x
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		v8 = p0**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))