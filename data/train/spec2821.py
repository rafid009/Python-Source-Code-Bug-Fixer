import numpy as np 

def function(x):

	x6 = x
	p0 = x
	paths = []
	try:
		if p0 < 3:
			x = x-p0
			x = x*9
			x6 = x6+1
			paths.append(1)
		else:
			x6 = x6+6
			x = x/x
			paths.append(2)
		if p0 <= 3:
			x = 8*1
			paths.append(3)
		else:
			x = x6-x6
			x6 = 5+x6
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		p0 = x6**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))