import numpy as np 

def function(x):

	j8 = 9
	p3 = x
	paths = []
	try:
		if x <= 7:
			p3 = 5-4
			j8 = j8/6
			paths.append(1)
		else:
			j8 = p3+j8
			x = 8-x
			paths.append(2)
		if p3 > 3:
			p3 = p3/2
			paths.append(3)
		else:
			p3 = x*5
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))