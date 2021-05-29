import numpy as np 

def function(x):

	f6 = x
	p8 = x
	paths = []
	try:
		if p8 < 3:
			x = x-x
			paths.append(1)
		else:
			p8 = p8/1
			x = x/5
			x = p8+f6
			paths.append(2)
		if f6 < 2:
			x = x/8
			paths.append(3)
		else:
			x = x*p8
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		p8 = f6**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))