import numpy as np 

def function(x):

	p8 = 2
	i5 = x
	paths = []
	try:
		if i5 > 2:
			x = p8-x
			p8 = p8-6
			paths.append(1)
		else:
			p8 = i5*0
			x = 7+x
			p8 = p8/7
			paths.append(2)
		if p8 < 0:
			i5 = p8/3
			paths.append(3)
		else:
			i5 = i5*4
			x = x-8
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))