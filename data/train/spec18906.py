import numpy as np 

def function(x):

	p9 = x
	j8 = 5
	paths = []
	try:
		if p9 > 7:
			j8 = j8+1
			p9 = p9*x
			paths.append(1)
		else:
			j8 = j8+j8
			paths.append(2)
		if x >= 3:
			j8 = x*x
			j8 = x-3
			j8 = j8/7
			paths.append(3)
		else:
			p9 = 5-p9
			j8 = j8*j8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))