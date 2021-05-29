import numpy as np 

def function(x):

	v2 = 1
	p8 = x
	paths = []
	try:
		if v2 <= 8:
			p8 = 6*7
			v2 = v2/x
			p8 = p8/2
			paths.append(1)
		else:
			p8 = x+p8
			p8 = p8-5
			paths.append(2)
		if p8 >= 5:
			v2 = 3+v2
			x = x+1
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))