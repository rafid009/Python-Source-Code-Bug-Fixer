import numpy as np 

def function(x):

	p9 = 9
	o4 = 5
	paths = []
	try:
		if p9 >= 8:
			x = 1-7
			p9 = x-1
			paths.append(1)
		else:
			p9 = 1+p9
			paths.append(2)
		if o4 > 0:
			p9 = p9/2
			paths.append(3)
		else:
			p9 = 4-7
			o4 = 1/4
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		o4 = p9**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))