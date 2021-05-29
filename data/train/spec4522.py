import numpy as np 

def function(x):

	j8 = 7
	p0 = x
	paths = []
	try:
		if p0 < 3:
			j8 = j8+0
			paths.append(1)
		else:
			j8 = j8/7
			j8 = j8+7
			p0 = 0*p0
			paths.append(2)
		if j8 < 3:
			j8 = j8*x
			p0 = p0+p0
			x = x*6
			paths.append(3)
		else:
			j8 = j8-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))