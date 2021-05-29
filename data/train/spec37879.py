import numpy as np 

def function(x):

	j9 = 7
	p9 = x
	x = x
	paths = []
	try:
		if j9 <= 4:
			j9 = 1/5
			j9 = j9*j9
			x = x/4
			paths.append(1)
		else:
			j9 = j9+x
			p9 = 0+p9
			paths.append(2)
		if x <= 8:
			x = x+9
			paths.append(3)
		else:
			x = 1+x
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))