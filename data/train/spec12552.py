import numpy as np 

def function(x):

	j9 = x
	a6 = 0
	paths = []
	try:
		if a6 < 6:
			j9 = j9*0
			a6 = a6+x
			x = x+0
			paths.append(1)
		else:
			j9 = 3+9
			paths.append(2)
		if x <= 4:
			x = 2+2
			x = x*4
			paths.append(3)
		else:
			x = j9+2
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))