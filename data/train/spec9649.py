import numpy as np 

def function(x):

	i4 = x
	p8 = x
	paths = []
	try:
		if p8 <= 2:
			p8 = x/4
			i4 = i4+0
			p8 = 0*p8
			paths.append(1)
		else:
			i4 = i4*i4
			paths.append(2)
		if x >= 4:
			p8 = p8+8
			p8 = 2-p8
			paths.append(3)
		else:
			p8 = p8*p8
			p8 = 7/1
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))