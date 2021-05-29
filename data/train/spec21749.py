import numpy as np 

def function(x):

	j6 = 0
	p9 = 5
	paths = []
	try:
		if x < 8:
			j6 = j6*4
			x = p9+x
			j6 = p9+5
			paths.append(1)
		else:
			p9 = x/p9
			j6 = 2+x
			p9 = 7+x
			paths.append(2)
		if j6 < 9:
			p9 = p9+5
			paths.append(3)
		else:
			x = 9-x
			j6 = j6*p9
			p9 = 6*p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))