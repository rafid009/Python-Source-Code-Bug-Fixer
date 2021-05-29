import numpy as np 

def function(x):

	p3 = x
	i6 = x
	paths = []
	try:
		if x >= 2:
			p3 = p3+3
			i6 = i6+5
			paths.append(1)
		else:
			x = x/8
			p3 = i6-3
			paths.append(2)
		if i6 > 3:
			x = i6*2
			x = x*0
			p3 = p3-x
			paths.append(3)
		else:
			p3 = x*1
			p3 = 5*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))