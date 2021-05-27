import numpy as np 

def function(x):

	j8 = 7
	p1 = 5
	paths = []
	try:
		if j8 > 8:
			x = x*3
			j8 = x-0
			paths.append(1)
		else:
			j8 = j8*9
			paths.append(2)
		if p1 < 7:
			j8 = j8+j8
			paths.append(3)
		else:
			x = x+1
			p1 = j8+p1
			p1 = 7*9
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